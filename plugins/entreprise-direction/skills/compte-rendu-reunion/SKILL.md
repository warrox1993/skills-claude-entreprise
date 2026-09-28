---
name: compte-rendu-reunion
description: "Transforme des notes brutes, une transcription ou un enregistrement retranscrit d'une réunion en compte rendu court et actionnable : décisions prises, actions avec responsable et échéance, points ouverts, informations clés, et un message de diffusion prêt à envoyer. À utiliser dès qu'on colle des notes de réunion, une transcription Teams, Zoom ou Meet, un procès-verbal à rédiger, ou qu'on demande un résumé, un PV, un compte rendu ou la liste des actions d'une réunion."
---

# Compte rendu de réunion avec décisions et actions

Un compte rendu utile se lit en deux minutes et répond à trois questions : qu'a-t-on décidé, qui fait quoi pour quand, et qu'est-ce qui reste ouvert. Le récit chronologique des échanges n'intéresse presque personne. Ce skill extrait l'essentiel, sans rien inventer, et rend visibles les trous (action sans responsable, décision ambiguë).

## Informations à rassembler

- Les notes ou la transcription
- Date, objet, participants et excusés si connus
- Le public du compte rendu (participants seulement, direction, conseil d'administration, toute l'équipe)
- Le format souhaité si l'organisation en a un (procès-verbal formel, compte rendu interne)

## Démarche

1. **Repérer les décisions.** Une décision est un choix acté (« on retient le fournisseur B »), pas une opinion exprimée. Si une décision semble prise mais que la formulation est ambiguë, classe-la dans les points à confirmer.
2. **Extraire les actions** : verbe d'action, responsable (une personne ou un rôle, pas « l'équipe »), échéance. Si le responsable ou l'échéance manque, écris `[à attribuer]` ou `[échéance à fixer]` : ces trous sont la principale cause d'actions oubliées.
3. **Lister les points ouverts** : questions non tranchées, informations attendues, sujets reportés.
4. **Garder les informations clés** : chiffres, dates, contraintes annoncées pendant la réunion, en une phrase chacune.
5. **Résumer en trois lignes** en tête, pour ceux qui ne liront que ça.
6. **Neutraliser** : pas d'attribution de propos polémiques à une personne quand ce n'est pas nécessaire, pas de jugement sur les participants. Un procès-verbal formel peut exiger d'attribuer les positions : suis alors la demande de l'utilisateur.
7. **Préparer le message de diffusion** : court, avec les actions en évidence et la date de la prochaine réunion.

## Format de sortie

Markdown :

1. En-tête : objet, date, participants, excusés, rédacteur `[à compléter]`
2. `## En bref` : 3 lignes maximum
3. `## Décisions` : liste numérotée
4. `## Actions` : tableau `N° | Action | Responsable | Échéance | Statut`
5. `## Points ouverts` : avec qui doit apporter la réponse
6. `## Informations à retenir`
7. `## Prochaine réunion`
8. `## Message de diffusion` : e-mail ou message prêt à envoyer

## Garde-fous

- N'invente ni décision, ni responsable, ni échéance. Ce qui n'est pas dans les notes est marqué comme manquant.
- Si la transcription contient des propos personnels ou sensibles sans rapport avec l'objet (santé d'un collègue, conflit personnel, évaluation individuelle), ne les reprends pas dans le compte rendu et signale-le à l'utilisateur.
- Si deux passages se contredisent, présente la contradiction dans les points ouverts au lieu de choisir.
- Signale si une décision paraît dépasser le pouvoir de la réunion (par exemple un engagement financier qui nécessite l'accord du conseil d'administration), sans trancher.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
