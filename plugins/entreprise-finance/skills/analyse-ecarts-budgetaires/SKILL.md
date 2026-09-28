---
name: analyse-ecarts-budgetaires
description: "Analyse les écarts entre budget et réalisé (ou entre deux périodes) et les explique dans une note courte destinée à la direction ou au conseil d'administration, avec chiffres vérifiés, causes probables, effets volume/prix, points à investiguer et actions proposées. À utiliser dès qu'on colle un tableau budget vs réel, un reporting mensuel, un export comptable ou qu'on demande pourquoi les chiffres s'écartent du prévisionnel, même sans employer le mot « écart »."
---

# Explication d'écarts budgétaires pour la direction

Une direction ne lit pas un tableau de cinquante lignes : elle veut savoir ce qui a bougé, pourquoi, si c'est durable et ce qu'on fait. Ce skill transforme un tableau budget/réalisé en une note d'une page, en partant des chiffres et en séparant clairement les faits, les hypothèses et les questions ouvertes.

## Informations à rassembler

- Le tableau (collé, CSV, Excel) avec au minimum : poste, budget, réalisé, et idéalement l'année précédente
- La période (mois, trimestre, cumul annuel) et l'unité (euros, milliers d'euros)
- Le contexte connu : événements du trimestre, décisions prises, saisonnalité
- Le seuil de matérialité si l'entreprise en a un ; sinon, propose-en un (par exemple 5 % et 10 000 euros) et dis-le

## Démarche

1. **Recalculer avant de commenter.** Calcule toi-même chaque écart en valeur et en pourcentage, les sous-totaux et le résultat. Si tu disposes d'un outil d'exécution de code, utilise-le pour les calculs sur plus de quelques lignes. Si les totaux fournis ne correspondent pas à la somme des lignes, signale-le en tête de note : une note bâtie sur un tableau faux est pire que pas de note.
2. **Orienter les écarts.** Indique pour chaque écart s'il est favorable ou défavorable au résultat (un dépassement de chiffre d'affaires est favorable, un dépassement de charges est défavorable). Ne te fie pas au signe seul.
3. **Filtrer par matérialité.** Ne commente que les écarts au-dessus du seuil ; regroupe le reste en une ligne.
4. **Décomposer quand c'est possible.** Si les quantités et les prix sont disponibles, sépare effet volume, effet prix et effet mix. Sinon, dis que la décomposition n'est pas possible avec les données fournies.
5. **Qualifier chaque écart** : ponctuel (événement non récurrent), décalage de calendrier (sera rattrapé), structurel (appelle une révision du budget ou une action). C'est ce qui intéresse le plus la direction.
6. **Distinguer faits et hypothèses.** Une cause donnée par l'utilisateur est un fait ; une cause que tu déduis est une hypothèse à confirmer et doit être présentée comme telle.
7. **Proposer des actions** proportionnées et assignables, et les questions à poser aux responsables de budget.

## Format de sortie

Markdown, une page :

1. `## En bref` : trois à cinq phrases avec l'écart sur le résultat, les deux ou trois causes principales et la tendance pour la fin de période
2. `## Écarts significatifs` : tableau `Poste | Budget | Réalisé | Écart | Écart % | Sens | Nature (ponctuel / calendrier / structurel) | Explication`
3. `## Ce que nous ne savons pas encore` : questions précises, avec la personne ou le service à interroger
4. `## Actions proposées` : puces avec responsable suggéré et échéance
5. `## Contrôles effectués` : une ou deux lignes (totaux recalculés, seuil utilisé, données manquantes)

Chiffres au format belge (espace pour les milliers, virgule décimale, symbole euro après le nombre).

## Garde-fous

- Tu expliques des chiffres ; tu ne fais ni audit, ni avis comptable ou fiscal. Un traitement comptable douteux (provision, activation d'une charge, rattachement de période) doit être signalé pour validation par le comptable ou l'expert-comptable.
- N'invente aucune cause. En l'absence d'information, écris « cause non documentée » et place la question dans la section correspondante.
- Si les données contiennent des noms de personnes (salaires individuels, primes), agrège-les dans la note : la direction a besoin de l'écart de masse salariale, pas du détail nominatif.
- Si les données semblent incohérentes (écart de 900 %, signe inversé), dis-le au lieu de construire une explication.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
