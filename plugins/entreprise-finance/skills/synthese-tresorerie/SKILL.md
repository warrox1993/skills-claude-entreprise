---
name: synthese-tresorerie
description: "Produit une synthèse de trésorerie lisible par un dirigeant de PME (position actuelle, prévision sur 13 semaines ou 3 à 6 mois, point bas, échéances à risque, leviers d'action) à partir de soldes bancaires, d'une balance âgée clients/fournisseurs ou d'un plan de trésorerie. À utiliser quand on parle de cash, de trésorerie, de liquidités, de besoin en fonds de roulement, de prévision d'encaissements et de décaissements ou de peur d'un découvert."
---

# Synthèse de trésorerie pour la direction

La trésorerie est le premier indicateur qui tue une PME rentable. Une synthèse utile répond à trois questions : combien avons-nous aujourd'hui, quel sera le point le plus bas dans les prochaines semaines, et que pouvons-nous faire si ce point est trop bas. Ce skill construit cette vue à partir des données disponibles, en rendant visibles les hypothèses.

## Informations à rassembler

- Soldes bancaires à une date précise (et lignes de crédit disponibles)
- Encaissements attendus : factures clients ouvertes avec échéances, ventes prévues, subsides
- Décaissements attendus : fournisseurs, salaires et précompte, ONSS, TVA, acomptes d'impôt, loyers, remboursements d'emprunt, investissements
- Horizon souhaité (par défaut 13 semaines) et seuil de sécurité de la direction (sinon, propose un mois de charges fixes)

S'il manque une grande masse (par exemple les salaires), demande-la : une prévision sans les salaires n'a pas de sens.

## Démarche

1. **Partir d'un solde vérifiable** à une date donnée. Tout le reste en découle.
2. **Construire la prévision** par semaine (13 semaines) ou par mois, en séparant encaissements et décaissements. Utilise un outil d'exécution de code si tu en as un et si les lignes sont nombreuses ; sinon, calcule pas à pas et vérifie les soldes cumulés.
3. **Appliquer des hypothèses d'encaissement réalistes.** Un client qui paie habituellement à 60 jours ne paiera pas à 30 parce que la facture le dit. Si l'historique est donné, utilise-le ; sinon, indique l'hypothèse retenue. Les factures déjà en retard important sont à traiter à part (scénario prudent).
4. **Repérer le calendrier belge des grosses sorties** que l'utilisateur doit confirmer : TVA (mensuelle ou trimestrielle), cotisations ONSS, précompte professionnel, versements anticipés d'impôt des sociétés, pécule de vacances et prime de fin d'année selon la période. Ne les invente pas : liste celles qui manquent.
5. **Faire deux scénarios** : central et prudent (retards clients, une rentrée incertaine qui glisse). Le point bas du scénario prudent est le chiffre que la direction doit regarder.
6. **Proposer des leviers** classés par délai d'effet : relances ciblées, acomptes à la commande, étalement fournisseur négocié, report d'investissement, mobilisation d'une ligne de crédit, plan d'apurement avec l'administration. Pour chacun, l'effet estimé et la contrepartie.

## Format de sortie

Markdown :

1. `## Situation au [date]` : solde, lignes disponibles, trésorerie totale mobilisable
2. `## Prévision` : tableau par semaine ou par mois `Période | Encaissements | Décaissements | Flux net | Solde fin de période (central) | Solde (prudent)`
3. `## Point bas et alertes` : date et montant du point bas, comparaison au seuil de sécurité, échéances qui posent problème
4. `## Hypothèses` : liste explicite, chacune modifiable
5. `## Leviers` : tableau `Levier | Effet estimé | Délai | Contrepartie ou risque`
6. `## Données manquantes` si nécessaire

Chiffres au format belge (espace pour les milliers, virgule décimale).

## Garde-fous

- Une prévision n'est pas une certitude : chaque montant non fourni par l'utilisateur est une hypothèse et doit apparaître comme telle.
- Tu ne donnes pas d'avis de financement définitif ni de conseil fiscal. Pour un crédit, un plan d'apurement ONSS ou TVA, ou une situation proche de la cessation de paiement, renvoie vers le comptable, la banque ou un accompagnement spécialisé (par exemple les centres pour entreprises en difficulté).
- Si la trésorerie devient négative dans le scénario central sans ligne de crédit pour la couvrir, dis-le clairement en tête de synthèse, sans dramatiser ni minimiser.
- Agrège les salaires : pas de montant individuel nominatif dans la synthèse.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
