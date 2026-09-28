---
name: revue-politique-mots-de-passe-mfa
description: "Relit une politique de mots de passe et d'authentification (MFA, gestionnaire de mots de passe, comptes administrateurs, comptes partagés, réinitialisation) et la compare aux recommandations actuelles (NIST SP 800-63B, guides du CCB et de l'ANSSI), puis propose une version corrigée et un plan de mise en œuvre réaliste. À utiliser dès qu'on colle une politique de sécurité, une charte informatique, des règles de mots de passe, ou qu'on demande si « changer le mot de passe tous les 90 jours » ou « 8 caractères avec majuscule et chiffre » est encore une bonne pratique."
---

# Revue d'une politique de mots de passe et de MFA

Beaucoup de politiques de mots de passe datent d'une époque où l'on pensait qu'imposer des symboles et un changement tous les 90 jours rendait les comptes plus sûrs. Les recommandations actuelles vont dans l'autre sens : longueur plutôt que complexité, pas de changement périodique sans raison, vérification contre les mots de passe déjà compromis, et surtout authentification multifacteur. Ce skill compare la politique existante à ces principes et propose une version applicable.

## Informations à rassembler

- La politique actuelle (texte, ou description des règles appliquées)
- L'environnement : Microsoft 365 / Entra ID, Google Workspace, annuaire local, applications métier, accès à distance
- Les utilisateurs : nombre, profils (bureau, terrain, externes), comptes administrateurs
- Les contraintes : applications anciennes sans MFA, postes partagés, budget

## Démarche

1. **Lire la politique règle par règle** et classer chaque règle : conforme aux recommandations actuelles, à modifier, à supprimer, manquante.
2. **Comparer aux repères suivants** (à vérifier dans les versions en vigueur, les documents de référence étant révisés) :
   - Longueur minimale plutôt que règles de composition : NIST SP 800-63B (révision 4) recommande au moins 15 caractères quand le mot de passe est le seul facteur, et au moins 8 quand il est utilisé avec un second facteur ; accepter des phrases de passe longues (la norme recommande d'autoriser au moins 64 caractères) et tous les caractères imprimables, espaces compris.
   - Pas d'obligation de composition (majuscule, chiffre, symbole) ni de changement périodique ; changement obligatoire en cas de suspicion de compromission.
   - Vérification des nouveaux mots de passe contre des listes de mots de passe connus ou compromis.
   - Limitation des tentatives de connexion plutôt que blocage agressif.
   - Pas d'indices ni de questions secrètes pour la réinitialisation.
   - MFA pour tous les accès distants, la messagerie et le cloud, et en priorité pour les comptes administrateurs ; méthodes résistantes à l'hameçonnage (clés FIDO2, passkeys) pour les comptes à privilèges ; se méfier du SMS comme seul second facteur pour ces comptes.
   - Gestionnaire de mots de passe fourni par l'entreprise, pour que chaque compte ait un mot de passe unique.
   - Comptes administrateurs séparés des comptes de travail quotidien ; pas de comptes partagés, ou alors gérés dans un coffre avec traçabilité.
   - Désactivation des protocoles d'authentification anciens qui contournent la MFA.
   - Procédure de réinitialisation qui vérifie l'identité du demandeur (cible fréquente de l'ingénierie sociale).
3. **Tenir compte du réel** : une règle inapplicable sera contournée. Prévois les exceptions (poste partagé en atelier, application ancienne) avec une mesure compensatoire.
4. **Rédiger la politique corrigée** en langage clair, courte, compréhensible par tout le personnel.
5. **Proposer un plan de mise en œuvre** par étapes : comptes administrateurs d'abord, puis messagerie et accès distants, puis le reste, avec communication aux utilisateurs.

## Format de sortie

Markdown :

1. `## Synthèse` : trois à cinq lignes, dont les deux ou trois changements les plus importants
2. `## Analyse règle par règle` : tableau `Règle actuelle | Verdict (garder / modifier / supprimer) | Pourquoi | Proposition`
3. `## Règles manquantes` : tableau `Règle à ajouter | Pourquoi | Priorité`
4. `## Politique révisée` : le texte complet, prêt à diffuser
5. `## Plan de mise en œuvre` : tableau `Étape | Contenu | Public | Durée estimée | Prérequis`
6. `## Points à vérifier` : paramètres techniques dans les outils concernés, versions des référentiels

## Garde-fous

- Ne demande jamais de mots de passe réels, ni de captures contenant des secrets. Si l'utilisateur en colle, dis-lui de les changer et ne les reprends pas.
- Cite les référentiels comme repères et invite à vérifier leur version courante ; ne présente pas une recommandation comme une obligation légale sauf si c'en est une pour l'organisation (par exemple l'authentification multifacteur dans les mesures NIS2).
- Reste neutre vis-à-vis des fournisseurs : pas de recommandation commerciale d'un produit précis sans que l'utilisateur le demande, et alors avec des alternatives.
- Pour un environnement complexe ou réglementé, recommande une validation par le responsable sécurité ou un prestataire spécialisé.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
