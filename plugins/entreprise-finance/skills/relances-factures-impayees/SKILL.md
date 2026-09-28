---
name: relances-factures-impayees
description: "Rédige une séquence graduée de relances pour factures impayées (rappel courtois, relance ferme, mise en demeure) adaptée au client, avec les mentions utiles du droit belge des retards de paiement (loi du 2 août 2002 entre entreprises, règles du Code de droit économique pour les consommateurs) à faire vérifier. À utiliser dès qu'on parle de facture en retard, d'impayé, de recouvrement amiable, de relance client, de rappel de paiement ou de mise en demeure."
---

# Relances de factures impayées, graduées

Relancer trop mollement laisse filer la trésorerie ; relancer trop durement abîme une relation client qui vaut souvent plus que la facture. Ce skill prépare une séquence de trois courriers (ou e-mails) dont le ton monte d'un cran à chaque étape, et qui rappellent au bon moment les conséquences prévues par la loi ou par les conditions générales.

## Informations à rassembler

- Client : entreprise (B2B) ou consommateur (B2C). La distinction change tout, demande-la si elle n'est pas claire.
- Numéro, date, montant et échéance de chaque facture ; relances déjà envoyées
- Ce que disent les conditions générales ou le contrat : délai de paiement, intérêts de retard, clause pénale
- Contexte de la relation : bon client en difficulté passagère, litige sur la prestation, client injoignable
- Coordonnées de la personne à contacter chez le créancier

## Démarche

1. **Vérifier qu'il n'y a pas de litige.** Si le client conteste la facture ou la prestation, une relance n'est pas la bonne réponse : propose plutôt un message qui traite la contestation, et signale-le.
2. **Choisir le cadre juridique à mentionner** (à faire valider, voir garde-fous) :
   - **Entre entreprises (B2B)** : la loi du 2 août 2002 concernant la lutte contre le retard de paiement dans les transactions commerciales prévoit, à défaut d'autre délai convenu, un paiement à 30 jours, des intérêts de retard dus de plein droit et sans mise en demeure au taux fixé semestriellement par le SPF Finances (sauf taux contractuel), et une indemnité forfaitaire de 40 euros pour frais de recouvrement, à laquelle peut s'ajouter une indemnisation raisonnable des autres frais justifiés. Depuis la loi du 14 août 2021, le délai de paiement contractuel ne peut en principe pas dépasser 60 jours.
   - **Envers un consommateur (B2C)** : le livre XIX du Code de droit économique encadre strictement le recouvrement. Le premier rappel doit être gratuit, le consommateur dispose d'un délai minimum de 14 jours calendrier après ce rappel (à compter du troisième jour ouvrable après l'envoi papier, ou du lendemain d'un envoi électronique) avant que des intérêts ou indemnités ne soient dus, et ceux-ci sont plafonnés selon le montant de la dette. N'annonce aucun frais dans le premier rappel B2C.
   N'annonce que ce qui est prévu par la loi ou les conditions générales du créancier, et indique la base (« conformément à nos conditions générales, article X »).
3. **Graduer.**
   - Relance 1, à l'échéance + quelques jours : courtoise, suppose un oubli, rappelle les références et les moyens de paiement, propose de signaler un problème.
   - Relance 2, environ deux semaines plus tard : ferme, factuelle, rappelle la première relance, annonce les conséquences prévues et une date limite précise.
   - Relance 3, mise en demeure : envoi recommandé ou par e-mail avec preuve, montant total détaillé (principal, intérêts, indemnité si applicables), dernier délai, suite envisagée (procédure de recouvrement, injonction, huissier, avocat), sans menace disproportionnée.
4. **Ouvrir une porte.** Dans les relances 1 et 2, propose un contact pour un plan d'apurement : un client qui paie en trois fois vaut mieux qu'un dossier contentieux.
5. **Adapter le ton** au contexte donné (client historique, première commande, contestation antérieure).

## Format de sortie

Pour chaque étape : un titre (`## Relance 1 : rappel amiable`, etc.), le moment d'envoi recommandé, le canal, l'objet, puis le texte complet prêt à envoyer avec les champs variables entre crochets. Termine par :

- `## Tableau de suivi` : `Étape | Date prévue | Canal | Montant réclamé | Envoyé le | Réponse`
- `## Points à faire vérifier` : taux d'intérêt en vigueur au semestre concerné, clauses exactes des conditions générales, montants maximaux B2C applicables, opportunité d'une procédure

## Garde-fous

- Ce n'est pas un avis juridique. Les références légales sont données pour être vérifiées par le service juridique, l'avocat ou le bureau de recouvrement ; rappelle-le en une ligne à la fin.
- N'invente jamais un taux, un montant d'indemnité ou une clause. Si le taux légal du semestre n'est pas fourni, laisse `[taux en vigueur à vérifier sur le site du SPF Finances]` et ne calcule pas les intérêts à l'aveugle.
- Pas de pression abusive : ni menace d'inscription sur une « liste noire », ni publicité de la dette, ni contact de tiers (employeur, voisins). Envers un consommateur, ces pratiques sont en outre interdites.
- Limite les données personnelles au strict nécessaire pour identifier la dette.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
