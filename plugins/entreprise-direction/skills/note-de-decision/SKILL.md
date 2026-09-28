---
name: note-de-decision
description: "Rédige une note de décision (ou note d'arbitrage) d'une à deux pages pour un comité de direction, un conseil d'administration ou un responsable : question posée, contexte, options comparées sur des critères explicites, risques, coûts, recommandation argumentée et ce qu'il faut décider, avant quand. À utiliser dès qu'il faut faire trancher un choix (fournisseur, investissement, organisation, lancement ou abandon d'un projet), préparer un arbitrage, présenter des options à la direction ou rédiger un « decision memo »."
---

# Note de décision

Une direction décide mieux quand on lui présente une question claire, des options réellement comparables et une recommandation assumée, plutôt qu'un dossier de trente pages. Ce skill structure la réflexion et rend visibles les critères et les incertitudes, pour que la décision puisse être expliquée ensuite.

## Informations à rassembler

- La décision à prendre, par qui, et avant quelle date
- Le contexte : pourquoi la question se pose maintenant
- Les options envisagées (y compris ne rien faire) et les informations disponibles sur chacune : coûts, délais, avantages, risques
- Les contraintes : budget, calendrier, obligations légales, capacité de l'équipe
- La préférence de l'auteur, s'il en a une

Si une seule option est présentée, ajoute au minimum l'option « statu quo » ou « reporter », et demande s'il existe une autre alternative réelle.

## Démarche

1. **Formuler la question en une phrase fermée** : « Faut-il remplacer notre ERP en 2027 par la solution X, pour un budget de 180 000 euros ? »
2. **Poser les critères avant de comparer** (coût total sur la durée, délai, risque, impact client ou personnel, réversibilité, alignement stratégique) et, si l'utilisateur l'accepte, leur pondération. Choisir les critères après coup revient à justifier une préférence.
3. **Comparer les options** sur ces critères, avec les chiffres fournis. Coût total sur plusieurs années plutôt que prix d'achat seul. Les calculs doivent être vérifiables.
4. **Analyser les risques** de chaque option : probabilité, impact, mesure d'atténuation. Mentionne aussi le risque de ne pas décider.
5. **Recommander** une option en expliquant le raisonnement et à quelles conditions la recommandation changerait. Une note sans recommandation renvoie le travail à la direction.
6. **Préciser ce qui est demandé** : décision attendue, budget à engager, prochaines étapes et responsable si la recommandation est suivie.
7. **Distinguer faits, estimations et opinions** tout au long de la note.

## Format de sortie

Markdown, deux pages au maximum :

1. `## Décision demandée` : une phrase, décideur, date limite
2. `## Contexte` : 5 à 8 lignes
3. `## Options` : une courte description de chacune
4. `## Comparaison` : tableau `Critère (poids) | Option A | Option B | Option C`
5. `## Risques` : tableau `Option | Risque | Probabilité | Impact | Atténuation`
6. `## Recommandation` : l'option, les raisons, les conditions qui la feraient changer
7. `## Si la recommandation est suivie` : prochaines étapes, responsables, calendrier
8. `## Incertitudes et informations manquantes`

## Garde-fous

- La décision appartient au décideur désigné ; la note éclaire, elle ne décide pas.
- N'invente aucun chiffre. Une estimation que tu proposes doit être marquée comme telle, avec sa méthode.
- Si une option pose une question juridique, fiscale, sociale (licenciement, changement de conditions de travail, consultation des organes de concertation) ou de sécurité, signale-le et recommande l'avis du spécialiste concerné avant la décision.
- Ne présente pas une option de façon volontairement défavorable pour pousser la recommandation : si l'utilisateur le demande, rappelle que la note perdra sa crédibilité.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
