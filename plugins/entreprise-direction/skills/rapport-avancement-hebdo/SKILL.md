---
name: rapport-avancement-hebdo
description: "Rédige le rapport d'avancement hebdomadaire d'un projet ou d'une équipe (météo globale, avancement par rapport au plan, réalisations, prochaines étapes, risques et blocages, décisions attendues du lecteur) à partir de notes, d'un export Jira/Trello/Planner ou d'un échange Slack/Teams. À utiliser dès qu'on demande un point hebdo, un weekly, un statut projet, un reporting de la semaine ou un rapport pour le sponsor ou le comité de pilotage."
---

# Rapport d'avancement hebdomadaire

Un rapport hebdomadaire ne sert pas à prouver qu'on a travaillé : il sert à ce que le lecteur (sponsor, direction, client) sache en une minute si le projet est sous contrôle et s'il doit agir. Ce skill produit ce rapport, honnête sur les retards et explicite sur ce qu'il attend du lecteur.

## Informations à rassembler

- Le projet, son objectif, ses jalons et la date de fin prévue
- Ce qui a été fait cette semaine et ce qui était prévu
- Les blocages, risques, retards et leurs causes
- Le budget consommé si suivi
- Le lecteur principal et ce qu'il peut débloquer

Si le plan de référence n'est pas fourni, compare avec le rapport précédent s'il existe ; sinon, dis que l'écart au plan ne peut pas être évalué.

## Démarche

1. **Donner une météo** globale et par axe (délai, budget, périmètre, qualité) : vert (sous contrôle), orange (risque identifié, plan d'action en cours), rouge (objectif menacé sans décision). Justifie chaque couleur en une phrase. Ne mets pas de vert par confort : un orange annoncé tôt vaut mieux qu'un rouge découvert tard.
2. **Comparer au plan** : jalons atteints, jalons glissés (de combien, pourquoi), impact sur la date finale.
3. **Lister les réalisations** en résultats, pas en activités (« recette du module facturation validée » plutôt que « tests en cours »).
4. **Lister les prochaines étapes** de la semaine suivante, avec responsables.
5. **Traiter les risques et blocages** : description, impact, action, responsable, date. Un blocage sans action ni demande est un constat inutile.
6. **Formuler les décisions ou aides attendues du lecteur** : c'est souvent la section la plus importante, place-la en haut si elle existe.
7. **Rester court** : une page. Les détails vont en annexe ou dans l'outil de suivi.

## Format de sortie

Markdown :

1. En-tête : projet, semaine (numéro et dates), auteur `[à compléter]`
2. `## Météo` : tableau `Axe | Couleur | Justification` (couleur écrite en toutes lettres : Vert / Orange / Rouge)
3. `## Ce que nous attendons de vous` : décisions ou aides demandées, avec échéance (ou « Rien cette semaine »)
4. `## Avancement par rapport au plan` : tableau `Jalon | Date prévue | Date prévue actualisée | Statut`
5. `## Réalisé cette semaine`
6. `## Prévu la semaine prochaine`
7. `## Risques et blocages` : tableau `Risque ou blocage | Impact | Action | Responsable | Échéance`

## Garde-fous

- N'embellis pas : si les informations indiquent un retard, la météo doit le refléter. Si l'utilisateur demande de masquer un problème, rappelle le risque de perte de confiance et propose une formulation factuelle et constructive.
- N'invente ni pourcentage d'avancement, ni date, ni chiffre budgétaire.
- Ne mets pas en cause des personnes nommément : décris les problèmes en termes de tâches, de dépendances ou de ressources. Les questions de performance individuelle se traitent ailleurs.
- Si un risque touche la sécurité, la conformité ou les données personnelles, signale-le explicitement même s'il paraît secondaire.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
