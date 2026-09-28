---
name: reponse-reclamation-client
description: "Rédige la réponse à une réclamation ou plainte client (e-mail, formulaire, avis en ligne, courrier) qui reconnaît le problème sans langue de bois, explique ce qui s'est passé, propose une solution concrète dans les limites fixées par l'entreprise et indique la suite, avec une note interne sur la cause et les engagements pris. À utiliser dès qu'on colle un message de client mécontent, un avis négatif, une plainte, un litige de livraison ou de facturation, ou qu'on demande « comment répondre à ce client »."
---

# Réponse à une réclamation client

Un client qui se plaint donne à l'entreprise une chance de le garder. Les réponses qui échouent sont celles qui se défendent, se cachent derrière une procédure ou promettent ce que personne n'a validé. Ce skill écrit une réponse humaine, précise et tenable, et prépare de quoi traiter la cause en interne.

## Informations à rassembler

- Le message du client (texte exact) et le canal (e-mail, avis public, téléphone retranscrit)
- Les faits vérifiés côté entreprise : commande, dates, ce qui a réellement mal tourné, ce qui relève du client
- Ce que l'entreprise peut offrir : remplacement, remboursement, geste commercial, délai, et qui doit l'approuver
- Le ton habituel de la marque (vouvoiement, signature)

Si les faits internes ne sont pas fournis, ne suppose pas : écris une réponse d'accusé de réception qui annonce une vérification et un délai de retour, et liste les informations à obtenir.

## Démarche

1. **Lire la réclamation deux fois** : ce qui est reproché, ce que le client demande explicitement, ce qu'il ressent. Repère les éléments factuels vérifiables et les éléments d'émotion.
2. **Qualifier la situation** : erreur de l'entreprise, responsabilité partagée, malentendu, demande non fondée. Ce classement guide le ton, jamais la politesse.
3. **Structurer la réponse** :
   - remercier brièvement et nommer précisément le problème (le client doit voir qu'il a été lu) ;
   - reconnaître ce qui est de la responsabilité de l'entreprise, sans excuses en boucle ni aveu au-delà des faits ;
   - expliquer en une ou deux phrases ce qui s'est passé, si c'est utile au client ;
   - proposer une solution concrète, datée, dans les limites autorisées ;
   - indiquer la suite et un contact nominatif ou un canal direct.
4. **Pour un avis public**, écrire une réponse plus courte, sans détail personnel ni numéro de commande, et proposer de poursuivre en privé.
5. **Pour une demande non fondée**, rester courtois et factuel, expliquer la règle appliquée, et proposer ce qui reste possible.
6. **Préparer la note interne** : cause probable, action corrective, engagements pris dans la réponse (qui fait quoi, quand).

## Format de sortie

1. `## Réponse au client` : objet (si e-mail) et texte complet, prêt à envoyer, champs variables entre crochets
2. `## Variante pour réponse publique` : seulement si la réclamation est publique
3. `## Note interne` : tableau `Élément | Contenu` avec : faits établis, faits à vérifier, cause probable, engagement pris, responsable, échéance, validation nécessaire (par exemple pour un geste commercial)

## Garde-fous

- Avant de rendre le texte, relis chaque affirmation concrète (qualité d'une personne ou d'une entreprise, engagement, condition, droit cédé, lieu, délai) et vérifie qu'elle vient de la demande. Ce qui est déduit ou supposé ne va pas dans le texte destiné au client : retire-le ou marque-le `[à confirmer]` et liste-le dans les points à vérifier. Le lecteur final prendra le texte au pied de la lettre.
- Ne promets aucun remboursement, délai ou geste commercial que l'utilisateur n'a pas indiqué comme possible ; propose-le plutôt dans la note interne comme option à valider.
- Pas de reconnaissance de responsabilité juridique au-delà des faits établis quand un dommage important est en jeu (blessure, perte financière élevée, menace de procédure) : dans ces cas, recommande une validation par la direction ou le service juridique avant envoi.
- Les droits légaux du consommateur (garantie légale de conformité de deux ans sur les biens, droit de rétractation pour la vente à distance) ne peuvent pas être refusés par une politique commerciale : si la demande du client s'appuie dessus, signale-le. Décris le droit sans y ajouter de modalités que l'entreprise n'a pas validées (qui paie le retour, enlèvement à domicile, délai de remboursement) : laisse-les `[à confirmer]`.
- Ne recopie pas de données personnelles inutiles, surtout dans une réponse publique.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
