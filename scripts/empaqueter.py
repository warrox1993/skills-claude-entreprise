#!/usr/bin/env python3
"""Crée un fichier .zip par skill, au format attendu par Claude.ai et Cowork.

Chaque archive contient le dossier du skill à sa racine (par exemple
offre-emploi-inclusive/SKILL.md et offre-emploi-inclusive/exemples/...), le nom du dossier
étant identique au champ name du SKILL.md.

Utilisation : python3 scripts/empaqueter.py [dossier-de-sortie]   (par défaut : dist/)
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def main() -> int:
    sortie = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "dist"
    sortie.mkdir(parents=True, exist_ok=True)
    skills = sorted(p.parent for p in RACINE.glob("plugins/*/skills/*/SKILL.md"))
    for dossier in skills:
        archive = sortie / f"{dossier.name}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for fichier in sorted(dossier.rglob("*")):
                if fichier.is_file():
                    zf.write(fichier, Path(dossier.name) / fichier.relative_to(dossier))
        print(archive)
    print(f"{len(skills)} archives créées dans {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
