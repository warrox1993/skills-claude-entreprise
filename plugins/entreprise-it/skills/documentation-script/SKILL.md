---
name: documentation-script
description: "Documente un script d'administration ou d'automatisation (PowerShell, Bash, Python, SQL, tâche planifiée) pour qu'un collègue puisse le comprendre, l'exécuter, le dépanner et le reprendre : rôle, prérequis, paramètres, effets de bord, exécution, planification, erreurs connues, retour arrière, plus un en-tête de commentaires à insérer dans le fichier. À utiliser dès qu'on colle un script en demandant une documentation, un README, un mode d'emploi, des commentaires, ou qu'on prépare une passation ou un départ."
---

# Documentation d'un script d'administration

Dans beaucoup d'entreprises, des scripts critiques tournent chaque nuit sans que personne d'autre que leur auteur ne sache ce qu'ils font. Le jour où ils échouent, ou où l'auteur part, on découvre qu'ils suppriment des fichiers, dépendent d'un compte personnel ou d'un chemin réseau disparu. Ce skill lit le script réellement, sans supposer, et produit la documentation qui permet à quelqu'un d'autre de le reprendre.

## Informations à rassembler

- Le script complet (ou le chemin du fichier si tu as accès au système de fichiers)
- Où et comment il s'exécute : serveur, tâche planifiée, cron, pipeline, compte d'exécution
- Le contexte métier : pourquoi il existe, qui dépend de son résultat
- Les incidents passés éventuels

## Démarche

1. **Lire tout le script** avant d'écrire. Identifie les entrées (paramètres, variables d'environnement, fichiers lus), les sorties (fichiers écrits, e-mails, bases modifiées), les dépendances (modules, outils, chemins réseau, comptes, API) et les actions destructrices (suppression, écrasement, arrêt de service).
2. **Décrire ce que le script fait réellement**, étape par étape, en langage clair. Si le code ne fait pas ce que suggère son nom ou ses commentaires, dis-le.
3. **Relever les risques** en les classant : sécurité (identifiants en clair, droits excessifs, entrées non validées), fiabilité (absence de gestion d'erreur, chemins en dur, pas de journalisation), exploitation (aucune alerte en cas d'échec, dépendance à un compte personnel).
4. **Rédiger le mode d'emploi** : comment l'exécuter manuellement, comment tester sans effet (s'il existe un mode simulation, sinon suggérer comment le faire en sécurité), comment vérifier que ça a marché.
5. **Documenter le dépannage** : erreurs probables, où regarder (journaux), comment revenir en arrière si le script a fait des dégâts.
6. **Produire un en-tête de commentaires** dans la syntaxe du langage (par exemple bloc d'aide `<# .SYNOPSIS … #>` pour PowerShell, docstring pour Python), sans modifier la logique.
7. **Proposer des améliorations**, séparées de la documentation, par ordre de priorité. N'applique aucune modification du code sans demande explicite.

## Format de sortie

1. `# [Nom du script]` puis une phrase de résumé
2. `## Rôle et contexte`
3. `## Fonctionnement` : étapes numérotées
4. `## Prérequis` : tableau `Élément | Détail` (système, modules, droits, comptes, chemins, connexions)
5. `## Paramètres et configuration` : tableau `Nom | Type | Défaut | Effet`
6. `## Effets et actions sensibles`
7. `## Exécution` : manuelle, planifiée, test sans risque, vérification du résultat
8. `## Dépannage` : tableau `Symptôme | Cause probable | Que faire`
9. `## Retour arrière`
10. `## Risques relevés` : tableau `Risque | Gravité | Recommandation`
11. `## En-tête à insérer dans le script` : bloc de code
12. `## Améliorations proposées` : liste par priorité

## Garde-fous

- Si le script contient un mot de passe, une clé d'API ou un jeton, ne le recopie pas dans la documentation (remplace-le par `[SECRET RETIRÉ]`), signale-le en risque de gravité haute et recommande de le révoquer et de le déplacer dans un coffre de secrets ou un gestionnaire d'identifiants.
- Ne dis pas qu'une commande est sans danger si tu n'en es pas sûr. En cas de doute sur l'effet d'une ligne (format produit, comportement selon la version ou la langue du système), écris-le au lieu d'affirmer.
- N'exécute pas le script pour « voir ce qu'il fait ».
- Les noms de serveurs, chemins et adresses internes restent dans une documentation interne : si l'utilisateur veut publier la documentation, rappelle de les anonymiser.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
