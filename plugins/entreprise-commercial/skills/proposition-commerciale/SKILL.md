---
name: proposition-commerciale
description: "Structure et rédige une proposition commerciale (offre, devis argumenté, réponse à une demande de prix) centrée sur le problème du client : contexte compris, solution proposée, périmètre et exclusions, planning, prix et conditions, hypothèses, prochaines étapes. À utiliser dès qu'on demande de rédiger une offre, une proposition, une réponse à un appel d'offres privé, un devis détaillé ou de transformer des notes de réunion client en document à envoyer."
---

# Proposition commerciale structurée

Beaucoup de propositions perdent parce qu'elles parlent du vendeur (historique, valeurs, liste de services) au lieu du client. Une bonne proposition commence par la reformulation du problème du client, dans ses mots, et rend le prix compréhensible en le reliant à ce que le client obtient. Elle protège aussi le vendeur en rendant explicites le périmètre, les exclusions et les hypothèses.

## Informations à rassembler

- Le client, son besoin exprimé et ce qu'il a dit en réunion (notes, e-mails)
- La solution envisagée, les livrables, le planning possible
- Le prix, son mode de calcul, les conditions (acompte, paiement, validité, révision)
- Ce qui est exclu, ce qui dépend du client
- Les éléments de preuve disponibles (références autorisées, certifications)

S'il manque le prix ou le périmètre, ne les invente pas : produis la structure avec des emplacements `[à compléter]` et liste les questions.

## Démarche

1. **Reformuler le besoin** en reprenant les enjeux du client (délais, coûts, risques) et, si possible, ses propres termes. Le client doit se dire « ils ont compris ».
2. **Présenter la solution** comme une réponse à ces enjeux, étape par étape, sans jargon.
3. **Délimiter le périmètre** : livrables inclus, exclusions explicites, prérequis côté client. C'est la section qui évite les litiges.
4. **Planifier** avec des jalons datés ou relatifs et les dépendances.
5. **Présenter le prix** de façon lisible : tableau par poste, total HTVA, TVA, total TVAC, conditions de paiement, durée de validité de l'offre. Si plusieurs options existent, trois au maximum, avec une recommandation.
6. **Lister les hypothèses** sur lesquelles le prix repose (volume, nombre de réunions, accès fournis). Une hypothèse qui ne tient plus justifie une révision.
7. **Terminer par une prochaine étape simple** : signature, réunion de lancement, date limite.
8. **Relire comme le client** : ce document répond-il à sa question sans avoir besoin du vendeur pour l'expliquer ?

## Format de sortie

Document Markdown prêt à mettre en page :

1. Titre, client, date, référence, validité
2. `## Votre situation`
3. `## Ce que nous proposons`
4. `## Périmètre` : `### Inclus`, `### Non inclus`, `### Ce que nous attendons de vous`
5. `## Planning` : tableau `Étape | Contenu | Durée ou date`
6. `## Investissement` : tableau `Poste | Quantité | Prix unitaire HTVA | Total HTVA`, puis sous-total, TVA, total TVAC, conditions
7. `## Hypothèses`
8. `## Pourquoi nous` : 3 puces factuelles maximum, uniquement avec des preuves fournies
9. `## Prochaines étapes`

Ensuite, hors document : `## Points à vérifier avant envoi` (taux de TVA applicable, conditions générales à joindre, validation interne du prix).

## Garde-fous

- Avant de rendre le texte, relis chaque affirmation concrète (qualité d'une personne ou d'une entreprise, engagement, condition, droit cédé, lieu, délai) et vérifie qu'elle vient de la demande. Ce qui est déduit ou supposé ne va pas dans le texte destiné au client : retire-le ou marque-le `[à confirmer]` et liste-le dans les points à vérifier. Le lecteur final prendra le texte au pied de la lettre.
- N'invente ni prix, ni référence client, ni certification, ni délai. Le taux de TVA est à confirmer par l'utilisateur (autoliquidation, taux réduit, client hors Belgique).
- Les conditions contractuelles importantes (responsabilité, pénalités, propriété intellectuelle, garantie) doivent renvoyer aux conditions générales de l'entreprise ou être validées par le service juridique ; ne rédige pas de clause juridique engageante de ton propre chef.
- Ne reprends pas d'information confidentielle d'un autre client dans la proposition.
- Si une promesse paraît intenable au vu des éléments fournis (délai, résultat garanti), signale-le avant de l'écrire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
