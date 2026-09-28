---
name: premiere-lecture-contrat
description: "Fait une première lecture structurée d'un contrat commercial (prestation de services, fourniture, licence SaaS, sous-traitance, NDA, bail commercial…) du point de vue de l'utilisateur, résume ses engagements et repère les clauses à risque ou inhabituelles, pour préparer les questions à poser à un juriste ou à un avocat. À utiliser dès qu'on colle un contrat, des conditions générales ou un projet d'accord en demandant « c'est ok ? », « qu'est-ce que je signe ? », « points d'attention », « relis ce contrat »."
---

# Première lecture d'un contrat

Beaucoup de PME signent des contrats sans les lire en entier, faute de temps ou de juriste interne. Ce skill ne remplace pas un conseil juridique : il fait le travail préparatoire qui rend ce conseil plus rapide et moins cher. Il résume ce que l'entreprise s'engage à faire, repère les clauses qui méritent attention et formule les questions à poser au professionnel.

## Informations à rassembler

- Le texte du contrat (et ses annexes, conditions générales auxquelles il renvoie)
- De quel côté se trouve l'utilisateur (client, fournisseur, bailleur…) et ce qu'il attend du contrat
- Le montant et la durée en jeu, l'importance stratégique
- Les points qui l'inquiètent déjà

Si des annexes ou conditions générales sont citées mais non fournies, signale-le dès le début : une partie des engagements peut s'y trouver.

## Démarche

1. **Identifier le contrat** : parties, objet, durée, prix, droit applicable, juridiction.
2. **Résumer les engagements de l'utilisateur** en langage courant : ce qu'il doit faire, payer, garantir, et jusqu'à quand.
3. **Passer en revue les clauses sensibles**, selon le type de contrat :
   - durée, reconduction tacite et préavis de résiliation ;
   - prix, indexation, révision, pénalités de retard ;
   - responsabilité : plafonds, exclusions, garanties données ;
   - propriété intellectuelle et confidentialité ;
   - données personnelles (existe-t-il un accord de sous-traitance au sens de l'article 28 du RGPD si des données sont traitées pour le compte de l'utilisateur ?) ;
   - exclusivité, non-concurrence, non-sollicitation du personnel ;
   - sous-traitance et cession du contrat ;
   - droit applicable et tribunal compétent, clause d'arbitrage ;
   - clauses déséquilibrées : entre entreprises, le Code de droit économique (depuis la loi du 4 avril 2019) interdit certaines clauses abusives et en présume d'autres abusives ; le nouveau Code civil belge (livre 5 sur les obligations, en vigueur depuis le 1er janvier 2023) peut aussi jouer. Signale les clauses qui paraissent déséquilibrées sans conclure sur leur validité.
4. **Noter l'absent** : ce qu'un contrat de ce type contient d'habitude et qui manque (niveau de service, procédure de réception, réversibilité des données en fin de contrat SaaS…).
5. **Classer les points** : à négocier, à clarifier, à accepter en connaissance de cause.
6. **Rédiger les questions pour le juriste**, précises et référencées par article.

## Format de sortie

Markdown :

1. Avertissement en une ligne : première lecture non juridique, à valider par un professionnel
2. `## Carte d'identité du contrat` : tableau `Élément | Contenu | Article`
3. `## Vos engagements en clair` : puces
4. `## Points d'attention` : tableau `Article | Ce que dit la clause | Pourquoi c'est à regarder | Priorité (haute / moyenne / basse) | Piste de négociation`
5. `## Ce qui manque`
6. `## Questions à poser à votre juriste ou avocat` : liste numérotée
7. `## Dates à retenir` : échéances de préavis, reconduction, révision de prix

## Garde-fous

- Tu ne dis jamais qu'un contrat est « bon », « valable » ou « sans risque », et tu ne conseilles pas de signer ou de ne pas signer. Tu décris, tu signales, tu questionnes.
- Cite toujours l'article concerné ; si tu n'es pas sûr d'avoir compris une clause, dis-le.
- Les références légales sont des pistes à faire vérifier : le droit évolue et dépend des faits.
- Pour un contrat de travail, un litige en cours ou un enjeu important, recommande explicitement un avocat ou le service juridique.
- Ne reproduis pas inutilement les données personnelles contenues dans le contrat (numéros de registre national, adresses privées).

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
