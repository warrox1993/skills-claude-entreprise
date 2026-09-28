---
name: registre-traitements-rgpd
description: "Aide une organisation à établir ou compléter son registre des activités de traitement (article 30 du RGPD) à partir d'une description de ses activités : une fiche par traitement avec finalité, base légale proposée, catégories de personnes et de données, destinataires, transferts hors EEE, durées de conservation, mesures de sécurité, et les questions ouvertes à trancher. À utiliser dès qu'on parle de RGPD, GDPR, registre des traitements, données personnelles d'employés, clients ou prospects, mise en conformité vie privée ou d'un contrôle de l'Autorité de protection des données."
---

# Registre des activités de traitement (RGPD)

L'article 30 du RGPD demande à la plupart des organisations de tenir un registre de leurs traitements de données personnelles. C'est aussi le meilleur point de départ pour savoir quelles données on détient, pourquoi, et combien de temps. Ce skill transforme une description en langage courant (« on a un CRM, on paie les salaires via un secrétariat social, on filme l'entrepôt ») en fiches structurées, et liste honnêtement ce qui reste à décider.

## Informations à rassembler

- L'organisation (nom, secteur, taille) et ses coordonnées de contact pour la protection des données ; délégué à la protection des données (DPO) s'il y en a un
- Les activités qui touchent des personnes : clients, prospects, personnel, candidats, fournisseurs, visiteurs, utilisateurs d'un site ou d'une application
- Les outils utilisés (logiciels, prestataires, hébergement) et le pays où les données sont stockées si connu
- Les pratiques de conservation et de sécurité actuelles

## Démarche

1. **Découper en traitements par finalité**, pas par logiciel : « gestion de la paie » et « recrutement » sont deux traitements même s'ils utilisent le même outil RH.
2. **Pour chaque traitement, remplir les éléments exigés par l'article 30.1** : responsable du traitement, finalités, catégories de personnes concernées, catégories de données, catégories de destinataires, transferts vers un pays tiers et garanties, délais d'effacement prévus, description générale des mesures de sécurité.
3. **Ajouter les éléments recommandés** en pratique (l'Autorité de protection des données publie un modèle) : base légale proposée (article 6, et article 9 pour les données sensibles), source des données, sous-traitants, existence d'un contrat de sous-traitance (article 28), nécessité éventuelle d'une analyse d'impact (AIPD).
4. **Proposer une base légale avec prudence** : présente-la comme une proposition et explique en une phrase pourquoi. Signale les pièges classiques : le consentement est rarement la bonne base pour les données du personnel ; l'intérêt légitime nécessite une mise en balance documentée ; la vidéosurveillance obéit en Belgique à une loi spécifique (loi caméras du 21 mars 2007) et, sur le lieu de travail, à la CCT n° 68.
5. **Proposer des durées de conservation** raisonnables quand l'utilisateur n'en a pas, en les marquant comme propositions, et en citant l'obligation légale quand tu es sûr qu'elle existe (par exemple les obligations comptables et sociales). En cas de doute, écris `[durée à confirmer]`.
6. **Lister les questions ouvertes et les actions** : contrats de sous-traitance manquants, transferts hors EEE à documenter, information des personnes à mettre à jour, AIPD à envisager.

## Format de sortie

Markdown :

1. `## Vue d'ensemble` : tableau `N° | Traitement | Personnes concernées | Base légale proposée | Niveau de priorité`
2. `## Fiches` : une sous-section par traitement, avec un tableau `Rubrique | Contenu` couvrant toutes les rubriques ci-dessus
3. `## Questions ouvertes` : numérotées, avec le traitement concerné
4. `## Actions recommandées` : tableau `Action | Pourquoi | Priorité`

Le contenu doit pouvoir être copié dans un tableur ou dans le modèle de registre de l'APD.

## Garde-fous

- C'est une aide à la documentation, pas un avis juridique ni une validation de conformité. Les bases légales et durées sont des propositions à valider par le DPO, un juriste ou un conseiller spécialisé.
- Ne demande pas et ne reproduis pas de données personnelles réelles : le registre décrit des catégories (« nom, adresse e-mail professionnelle »), jamais des personnes.
- Signale clairement les traitements à risque (données de santé, biométrie, surveillance des employés, profilage, données d'enfants) comme nécessitant un examen spécialisé.
- Ne présume pas qu'un prestataire est conforme : indique ce qu'il faut vérifier (contrat, localisation, garanties de transfert).
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
