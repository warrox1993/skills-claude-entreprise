#!/usr/bin/env python3
"""Valide la structure du dépôt : marketplace, plugins et skills.

Contrôles effectués :
- .claude-plugin/marketplace.json : champs obligatoires, chaque plugin pointe vers un dossier existant
  dont le plugin.json porte le même nom ;
- plugin.json de chaque plugin : nom en kebab-case, description, version, licence ;
- SKILL.md de chaque skill : frontmatter YAML valide, champs name et description présents,
  name identique au nom du dossier, 64 caractères au plus, minuscules, chiffres et tirets,
  sans les mots réservés « anthropic » et « claude », description non vide de 1024 caractères
  au plus, sans balise XML ;
- sections attendues dans chaque SKILL.md (format de sortie et garde-fous), et principes communs
  présents dans les garde-fous (marqueurs [à compléter] et [à vérifier]) ;
- présence de exemples/entree.md et exemples/sortie-attendue.md ;
- absence de tiret cadratin dans le README.

Utilisation : python3 scripts/valider.py  (code de sortie 1 en cas d'erreur)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
NOM_VALIDE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
BALISE_XML = re.compile(r"<[^>]+>")
MOTS_RESERVES = ("anthropic", "claude")
CHAMPS_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SECTIONS_OBLIGATOIRES = ("## Format de sortie", "## Garde-fous")
MARQUEURS_GARDE_FOUS = ("[à compléter]", "[à vérifier]", "Principes communs")

erreurs: list[str] = []


def erreur(chemin: Path, message: str) -> None:
    erreurs.append(f"{chemin.relative_to(RACINE)} : {message}")


def lire_json(chemin: Path) -> dict | None:
    try:
        return json.loads(chemin.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        erreur(chemin, f"JSON illisible ({exc})")
        return None


def verifier_nom(chemin: Path, nom: object, contexte: str) -> None:
    if not isinstance(nom, str) or not nom:
        erreur(chemin, f"{contexte} : nom absent")
        return
    if len(nom) > 64:
        erreur(chemin, f"{contexte} : nom de plus de 64 caractères")
    if not NOM_VALIDE.match(nom):
        erreur(chemin, f"{contexte} : nom « {nom} » invalide (minuscules, chiffres et tirets uniquement)")


def verifier_skill(dossier: Path) -> None:
    fichier = dossier / "SKILL.md"
    if not fichier.is_file():
        erreur(dossier, "SKILL.md manquant")
        return
    texte = fichier.read_text(encoding="utf-8")
    morceaux = texte.split("---", 2)
    if not texte.startswith("---") or len(morceaux) < 3:
        erreur(fichier, "frontmatter YAML absent ou non fermé")
        return
    try:
        meta = yaml.safe_load(morceaux[1])
    except yaml.YAMLError as exc:
        erreur(fichier, f"frontmatter YAML invalide ({exc})")
        return
    if not isinstance(meta, dict):
        erreur(fichier, "frontmatter vide ou mal formé")
        return

    inconnus = set(meta) - CHAMPS_FRONTMATTER
    if inconnus:
        erreur(fichier, f"champs de frontmatter non prévus : {', '.join(sorted(inconnus))}")

    nom = meta.get("name")
    verifier_nom(fichier, nom, "skill")
    if isinstance(nom, str):
        if nom != dossier.name:
            erreur(fichier, f"name « {nom} » différent du dossier « {dossier.name} »")
        for mot in MOTS_RESERVES:
            if mot in nom:
                erreur(fichier, f"name contient le mot réservé « {mot} »")
        if BALISE_XML.search(nom):
            erreur(fichier, "name contient une balise XML")

    description = meta.get("description")
    if not isinstance(description, str) or not description.strip():
        erreur(fichier, "description absente ou vide")
    else:
        if len(description) > 1024:
            erreur(fichier, f"description trop longue ({len(description)} caractères, maximum 1024)")
        if BALISE_XML.search(description):
            erreur(fichier, "description contient une balise XML")

    corps = morceaux[2]
    for section in SECTIONS_OBLIGATOIRES:
        if section not in corps:
            erreur(fichier, f"section « {section} » manquante")
    if "## Garde-fous" in corps:
        garde_fous = corps.split("## Garde-fous", 1)[1].split("\n## ", 1)[0]
        for marqueur in MARQUEURS_GARDE_FOUS:
            if marqueur not in garde_fous:
                erreur(fichier, f"garde-fous : marqueur « {marqueur} » absent")
    if len(corps.splitlines()) > 500:
        erreur(fichier, "corps de plus de 500 lignes : découper en fichiers de référence")

    for exemple in ("entree.md", "sortie-attendue.md"):
        chemin = dossier / "exemples" / exemple
        if not chemin.is_file() or not chemin.read_text(encoding="utf-8").strip():
            erreur(dossier, f"exemples/{exemple} manquant ou vide")


def verifier_plugin(dossier: Path, nom_attendu: str) -> int:
    manifeste = dossier / ".claude-plugin" / "plugin.json"
    if not manifeste.is_file():
        erreur(dossier, ".claude-plugin/plugin.json manquant")
        return 0
    donnees = lire_json(manifeste)
    if donnees is None:
        return 0
    verifier_nom(manifeste, donnees.get("name"), "plugin")
    if donnees.get("name") != nom_attendu:
        erreur(manifeste, f"name « {donnees.get('name')} » différent de l'entrée de la marketplace « {nom_attendu} »")
    for champ in ("description", "version", "license"):
        if not donnees.get(champ):
            erreur(manifeste, f"champ « {champ} » manquant")

    dossiers_skills = sorted(p for p in (dossier / "skills").glob("*") if p.is_dir())
    if not dossiers_skills:
        erreur(dossier, "aucun skill dans skills/")
    for skill in dossiers_skills:
        verifier_skill(skill)
    return len(dossiers_skills)


def main() -> int:
    marketplace = RACINE / ".claude-plugin" / "marketplace.json"
    donnees = lire_json(marketplace)
    if donnees is None:
        return 1
    verifier_nom(marketplace, donnees.get("name"), "marketplace")
    if not isinstance(donnees.get("owner"), dict) or not donnees["owner"].get("name"):
        erreur(marketplace, "owner.name manquant")
    plugins = donnees.get("plugins") or []
    if not plugins:
        erreur(marketplace, "aucun plugin déclaré")

    total_skills = 0
    declares = set()
    for entree in plugins:
        nom = entree.get("name")
        source = entree.get("source")
        declares.add(nom)
        if not isinstance(source, str) or not source.startswith("./"):
            erreur(marketplace, f"plugin « {nom} » : source relative attendue (./...)")
            continue
        dossier = (RACINE / source).resolve()
        if RACINE not in dossier.parents or not dossier.is_dir():
            erreur(marketplace, f"plugin « {nom} » : dossier source introuvable ({source})")
            continue
        total_skills += verifier_plugin(dossier, nom)

    for dossier in sorted((RACINE / "plugins").glob("*")):
        if dossier.is_dir() and dossier.name not in declares:
            erreur(dossier, "plugin présent sur le disque mais absent de marketplace.json")

    readme = RACINE / "README.md"
    if readme.is_file() and "\u2014" in readme.read_text(encoding="utf-8"):
        erreur(readme, "tiret cadratin présent")

    if erreurs:
        print(f"{len(erreurs)} erreur(s) :")
        for ligne in erreurs:
            print(f"  - {ligne}")
        return 1
    print(f"Validation réussie : {len(plugins)} plugins, {total_skills} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
