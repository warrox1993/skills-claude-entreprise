# Registre des activités de traitement (art. 30 RGPD) : salle d'escalade, Liège

> **À lire d'abord.** Ce document vous aide à constituer le registre. Ce n'est ni un avis juridique ni une validation de conformité. Les bases légales et les durées de conservation sont des **propositions** à faire valider par un juriste ou un conseiller spécialisé en protection des données.
>
> **Pourquoi vous devez tenir ce registre alors que vous avez moins de 250 salariés :** l'exemption de l'art. 30.5 ne s'applique pas à vous. Vos traitements sont réguliers, ils portent sur des données de santé (déclaration cardiaque, fiches médicales) et ils incluent de la vidéosurveillance.
>
> **Responsable du traitement (même valeur pour toutes les fiches) :** [dénomination] SRL, [adresse du siège], BCE [n°], contact vie privée : [nom ou fonction + e-mail dédié, par ex. privacy@…]. **DPO :** probablement pas obligatoire, car vos données de santé ne sont pas traitées « à grande échelle » au cœur de votre activité. Consignez ce raisonnement par écrit et désignez un référent interne.

## Vue d'ensemble

| N° | Traitement | Personnes concernées | Base légale proposée | Priorité |
|---|---|---|---|---|
| 1 | Inscription et gestion des membres | Membres, parents des mineurs, contacts d'urgence | Contrat (6.1.b) ; intérêt légitime pour le contact d'urgence (6.1.f) | Haute |
| 2 | Décharge et déclaration de santé (cardiaque) | Membres, mineurs | Contrat / intérêt légitime + art. 9 à déterminer | **Très haute** (santé) |
| 3 | Abonnements, facturation, domiciliation | Membres, titulaires de compte | Contrat (6.1.b) + obligation légale comptable (6.1.c) | Haute |
| 4 | Contrôle d'accès par badge | Membres, personnel éventuellement | Contrat / intérêt légitime (6.1.f) | Moyenne |
| 5 | Vidéosurveillance (accueil + parking) | Membres, visiteurs, personnel, passants | Intérêt légitime (6.1.f) dans le cadre de la loi caméras + CCT 68 | **Très haute** |
| 6 | Newsletter mensuelle | Membres (et ex-membres ?) | Soft opt-in clients / intérêt légitime, avec opt-out | Haute |
| 7 | Gestion du personnel et paie | Salariés, ex-salariés, ayants droit | Contrat de travail + obligations légales | Haute |
| 8 | Planning du personnel | Salariés | Contrat de travail (6.1.b) | Basse |
| 9 | Stages enfants (inscription + fiche médicale) | Enfants, parents [personnes autorisées à reprendre l'enfant : à confirmer] | Contrat + art. 9 à déterminer | **Très haute** (enfants + santé) |
| 10 | Photos : stages et événements, Instagram | Membres, enfants, participants | Consentement (6.1.a) + droit à l'image | Haute |
| 11 | Site web WordPress (formulaires, cookies) | Visiteurs du site, candidats membres | Selon l'usage (voir la fiche) | Moyenne |

## Fiches

### 1. Inscription et gestion des membres

| Rubrique | Contenu |
|---|---|
| Finalités | Enregistrer l'adhésion, identifier le membre, le contacter pour la gestion courante, prévenir un proche en cas d'accident |
| Personnes concernées | Membres majeurs et mineurs ; parent ou représentant légal des moins de 16 ans ; personnes à contacter en cas d'urgence (des tiers qui n'ont rien signé) |
| Données | Identité (nom, prénom, date de naissance), adresse, e-mail, téléphone ; identité et téléphone du contact d'urgence ; identité et signature du parent |
| Source | Le membre lui-même via le formulaire WordPress ; le parent pour les mineurs |
| Base légale proposée | **Contrat (6.1.b)** pour les données d'adhésion. **Intérêt légitime (6.1.f)** pour le contact d'urgence, qui reste limité au nom et au téléphone. Pour les mineurs, la signature du parent relève de la capacité juridique à contracter. Ce n'est pas un « consentement RGPD ». |
| Destinataires | Personnel d'accueil ; prestataires : hébergeur du site, extension de formulaire WordPress, logiciel de gestion (NL) |
| Contrat art. 28 | À vérifier avec l'hébergeur web, l'éditeur de l'extension de formulaire s'il stocke des données et le logiciel de gestion |
| Transferts hors EEE | À vérifier : localisation de l'hébergeur web, éventuel service tiers de formulaire ou d'anti-spam (reCAPTCHA = Google, États-Unis) |
| Conservation | Durée de l'affiliation, puis **[proposition : 1 an]** pour gérer une réinscription ou un litige, puis suppression. Supprimer les soumissions stockées dans WordPress dès leur transfert dans le logiciel de gestion **[à confirmer]**. |
| Sécurité | À décrire : HTTPS, comptes nominatifs, mises à jour de WordPress et des extensions, accès limité à l'accueil |
| Vigilance | Données de mineurs. Le contact d'urgence doit pouvoir être informé : ajoutez une mention du type « vous confirmez avoir informé cette personne ». |

### 2. Décharge et déclaration de santé cardiaque

| Rubrique | Contenu |
|---|---|
| Finalités | Informer le membre des risques, obtenir sa reconnaissance des risques et vérifier l'absence de contre-indication connue |
| Personnes concernées | Membres, y compris les mineurs, déclaration signée par le parent |
| Données | Signature, date, **information de santé (problèmes cardiaques : oui/non, détails ?)** = **donnée sensible (art. 9)** |
| Source | Le membre ou son parent |
| Base légale proposée | Art. 6 : contrat ou intérêt légitime (sécurité). Art. 9 : **à trancher avec un conseiller**. Pistes : consentement explicite (9.2.a), mais il doit être libre alors qu'il conditionne l'accès ; ou 9.2.f (constatation ou défense d'un droit en justice) pour la décharge. **Piste la plus simple : ne plus collecter l'information de santé.** Remplacez-la par une attestation du type « je déclare ne pas avoir de contre-indication médicale à la pratique de l'escalade ou avoir consulté un médecin ». |
| Destinataires | Direction ; assureur et avocat en cas de sinistre |
| Contrat art. 28 | Idem fiche 1 si la décharge est signée en ligne |
| Transferts hors EEE | Idem fiche 1 |
| Conservation | Décharge : **[durée à confirmer avec votre assureur ou avocat]** selon les délais de prescription en responsabilité. Pour les mineurs, la prescription peut être suspendue jusqu'à leur majorité. Détail médical : ne pas le conserver au-delà du nécessaire, idéalement ne pas le collecter du tout. |
| Sécurité | À mettre en place [proposition] : accès restreint à la direction, pas de visibilité au comptoir |
| Vigilance | **Examen spécialisé recommandé** : données de santé, de mineurs, et validité juridique de la décharge. Documentez s'il faut ou non une AIPD. |

### 3. Abonnements, facturation, domiciliation

| Rubrique | Contenu |
|---|---|
| Finalités | Gérer les formules d'abonnement, facturer, encaisser par domiciliation SEPA, suivre les impayés, tenir la comptabilité |
| Personnes concernées | Membres ; titulaires du compte bancaire, par exemple le parent |
| Données | Identité, formule, historique de paiements, IBAN, mandat SEPA, impayés |
| Source | Le membre ; la banque (retours de domiciliation) |
| Base légale proposée | Contrat (6.1.b) ; obligation légale comptable (6.1.c) ; intérêt légitime pour le recouvrement (6.1.f) |
| Destinataires | Logiciel de gestion (NL, sous-traitant) ; banque et éventuel prestataire de paiement (responsables distincts) ; comptable ou expert-comptable ; en cas de recouvrement, huissier ou société de recouvrement |
| Contrat art. 28 | **À vérifier** avec l'éditeur du logiciel de gestion, y compris sa liste de sous-traitants ultérieurs (hébergement cloud, e-mails transactionnels) ; avec le comptable s'il n'agit pas comme responsable distinct |
| Transferts hors EEE | Pays-Bas = UE, donc pas de transfert. Vérifier toutefois les sous-traitants ultérieurs de l'éditeur (support, hébergeur américain ?). |
| Conservation | Pièces comptables : **10 ans** (Code de droit économique, art. III.88) **[à confirmer avec votre comptable]**. Mandat SEPA : durée du mandat + **[délai à confirmer avec la banque]**. Données de gestion hors comptabilité : comme la fiche 1. |
| Sécurité | À décrire : double authentification sur le logiciel, un compte par employé, droits différenciés |
| Vigilance | Aucune particulière au-delà du contrat avec l'éditeur |

### 4. Contrôle d'accès par badge

| Rubrique | Contenu |
|---|---|
| Finalités | Réserver l'accès aux membres en ordre d'abonnement ; sécurité (savoir qui est présent) ; [statistiques de fréquentation : à confirmer] |
| Personnes concernées | Membres ; **salariés s'ils badgent aussi** |
| Données | N° de badge lié au membre, date et heure de passage, statut d'accès (autorisé ou refusé) |
| Source | Le système de badge |
| Base légale proposée | Contrat (6.1.b) pour le contrôle d'accès ; intérêt légitime (6.1.f) pour la sécurité et les statistiques |
| Destinataires | Accueil, direction, fournisseur du système (sous-traitant s'il a accès à distance) |
| Contrat art. 28 | Fournisseur du système de badge ou logiciel de gestion s'il est intégré |
| Transferts hors EEE | À vérifier |
| Conservation | Historique nominatif : **[proposition : 3 mois]**. Statistiques : anonymisées ou agrégées, sans limite. |
| Sécurité | À mettre en place [proposition] : accès restreint aux historiques |
| Vigilance | L'historique ne doit pas servir à surveiller les membres ni les salariés à d'autres fins. S'il sert au temps de travail du personnel, cela devient un traitement RH à informer et à encadrer. Vérifier que le système n'est **pas biométrique** (empreinte, visage). |

### 5. Vidéosurveillance (accueil + parking)

| Rubrique | Contenu |
|---|---|
| Finalités | Prévenir et constater les vols, les dégradations et les agressions ; sécurité des personnes et des biens |
| Personnes concernées | Membres, visiteurs, **personnel d'accueil**, passants sur le parking |
| Données | Images (enregistrées ? en direct ? son ? à préciser) |
| Source | Caméras |
| Base légale proposée | Intérêt légitime (6.1.f), **dans le cadre obligatoire de la loi caméras du 21 mars 2007** et, pour le personnel filmé, de la **CCT n° 68** |
| Destinataires | Direction ; police sur réquisition ; installateur ou mainteneur (sous-traitant) |
| Contrat art. 28 | Installateur ou mainteneur ; fournisseur cloud si les images sont stockées en ligne |
| Transferts hors EEE | À vérifier si enregistreur ou application cloud (fabricants hors UE fréquents) |
| Conservation | **1 mois maximum** (loi caméras), sauf si les images servent de preuve d'une infraction, d'un dommage ou pour identifier un auteur |
| Sécurité | À mettre en place si les images sont enregistrées (voir question 4) [proposition] : enregistreur sous clé, mot de passe changé par rapport à celui d'usine, accès limité à 1 ou 2 personnes, journal des consultations |
| Vigilance | **Examen spécialisé recommandé.** Obligations de la loi caméras à vérifier : déclaration à la police (declarationcamera.be) et validation annuelle ; pictogramme réglementaire ; registre spécifique des traitements d'images ; qualification de chaque lieu (voir question 3). CCT 68 : information préalable des salariés ; la caméra ne doit pas viser le poste de travail en continu. |

### 6. Newsletter mensuelle (Mailchimp)

| Rubrique | Contenu |
|---|---|
| Finalités | Informer les membres (actualités, événements [contenu promotionnel éventuel à confirmer, voir question 6]) |
| Personnes concernées | Membres ; ex-membres ? |
| Données | Nom, e-mail, statistiques d'ouverture et de clic (pixels de suivi) |
| Source | Fichier membres |
| Base légale proposée | Pour les membres : **exception « clients »** (soft opt-in, Code de droit économique art. XII.13 et arrêté royal du 4 avril 2003) si le contenu porte sur vos propres services similaires. Conditions : case d'opposition proposée à l'inscription et lien de désinscription dans chaque envoi. Sinon : consentement (6.1.a). |
| Destinataires | Mailchimp (Intuit Inc., États-Unis), sous-traitant |
| Contrat art. 28 | Accepter ou archiver le DPA de Mailchimp |
| Transferts hors EEE | **Oui, États-Unis.** Vérifier la certification d'Intuit au Data Privacy Framework UE–États-Unis ; à défaut, clauses contractuelles types. Le mentionner dans la politique de confidentialité. |
| Conservation | Jusqu'à la désinscription. Ex-membres : **[proposition : 2 ans après la fin de l'affiliation, puis suppression]**. |
| Sécurité | À mettre en place [proposition] : double authentification sur le compte Mailchimp, pas d'export inutile |
| Vigilance | Aujourd'hui, tous les membres sont inscrits d'office : vérifiez que l'opposition leur a bien été proposée. Les pixels de suivi sont à mentionner dans l'information. |

### 7. Gestion du personnel et paie

| Rubrique | Contenu |
|---|---|
| Finalités | Contrats, Dimona, paie, déclarations sociales et fiscales, absences, assurance accidents du travail |
| Personnes concernées | Salariés, ex-salariés, [étudiants jobistes éventuels, à confirmer], ayants droit (situation familiale pour le précompte) |
| Données | Identité, n° de registre national, coordonnées, IBAN, rémunération, situation familiale, **certificats médicaux (santé, art. 9)**, éventuels accidents du travail |
| Source | Le salarié ; le secrétariat social ; les organismes sociaux |
| Base légale proposée | Contrat de travail (6.1.b) ; obligations légales sociales et fiscales (6.1.c) ; art. 9.2.b (droit du travail) pour les certificats médicaux. **Pas le consentement.** |
| Destinataires | Secrétariat social ; ONSS, SPF Finances ; assureur accidents du travail ; service externe de prévention (SEPPT) ; caisse d'allocations familiales |
| Contrat art. 28 | Avec le secrétariat social. Son rôle (sous-traitant ou responsable distinct pour certaines missions légales) est à clarifier dans votre contrat. |
| Transferts hors EEE | En principe non, à vérifier auprès du secrétariat social |
| Conservation | Documents sociaux : **5 ans** ; pièces fiscales et comptables : **jusqu'à 10 ans**. **[À confirmer avec le secrétariat social.]** Dossier personnel : fin du contrat + délai de prescription **[à confirmer]**. |
| Sécurité | À mettre en place [proposition] : dossiers papier sous clé ; accès réservé à la direction |
| Vigilance | Certificats médicaux : ne conserver que le strict nécessaire |

### 8. Planning du personnel (Google Sheets)

| Rubrique | Contenu |
|---|---|
| Finalités | Organiser les horaires et les remplacements |
| Personnes concernées | Salariés |
| Données | Nom, horaires, absences (sans le motif médical) |
| Source | Direction, salariés |
| Base légale proposée | Contrat de travail (6.1.b) |
| Destinataires | Équipe ; Google (sous-traitant) |
| Contrat art. 28 | Assuré si Google Workspace avec avenant de traitement accepté. **Pas de DPA avec un compte Gmail personnel.** |
| Transferts hors EEE | Oui, possiblement vers les États-Unis (Google est certifié Data Privacy Framework, à vérifier) |
| Conservation | **[Proposition : 1 an]** ; au-delà, les données utiles à la paie sont chez le secrétariat social. Vérifiez vos obligations sur les horaires (règlement de travail, horaires variables) **[à confirmer]**. |
| Sécurité | À mettre en place [proposition] : partage nominatif, pas de lien public, double authentification |
| Vigilance | N'y indiquez pas le motif des absences (« malade », etc.) |

### 9. Stages enfants

| Rubrique | Contenu |
|---|---|
| Finalités | Inscrire l'enfant, assurer sa sécurité, réagir en cas de problème médical [remise de l'enfant aux personnes autorisées : à confirmer] |
| Personnes concernées | Enfants, parents [personnes autorisées à venir chercher l'enfant, médecin traitant : selon le contenu réel de la fiche, à confirmer] |
| Données | Identité et âge de l'enfant, coordonnées des parents, **fiche médicale : allergies, traitements, pathologies (art. 9)**, autorisation photo, paiement |
| Source | Parents |
| Base légale proposée | Contrat (6.1.b) pour l'inscription. Fiche médicale : **consentement explicite du parent (9.2.a)**, avec 9.2.c (intérêts vitaux) en situation d'urgence. **À valider par un conseiller.** |
| Destinataires | Moniteurs du stage, uniquement les informations utiles ; services de secours en cas d'urgence ; assureur en cas d'accident |
| Contrat art. 28 | Selon l'outil d'inscription (formulaire, logiciel de gestion ?) |
| Transferts hors EEE | À vérifier selon l'outil |
| Conservation | Fiche médicale : **destruction à la fin du stage + [proposition : 1 mois]**, sauf incident. Inscription et paiement : comme les fiches 1 et 3. |
| Sécurité | À mettre en place (voir question 8) [proposition] : fiches papier dans une farde fermée, sous la responsabilité du moniteur principal ; pas d'envoi via WhatsApp personnel |
| Vigilance | **Examen spécialisé recommandé** : données de santé d'enfants. Moniteurs externes ou étudiants : prévoir un engagement de confidentialité. |

### 10. Photos (stages, événements, Instagram)

| Rubrique | Contenu |
|---|---|
| Finalités | Communication de la salle : Instagram [autres supports éventuels à confirmer] |
| Personnes concernées | Membres, participants aux événements, **enfants des stages** |
| Données | Images identifiables [prénoms en légende ? à confirmer] |
| Source | [Auteur des photos à confirmer : personnel, bénévoles, participants ?] |
| Base légale proposée | **Consentement (6.1.a)**, qui répond aussi au droit à l'image. Pour les enfants : consentement du parent, **distinct par usage** (usage interne / site / réseaux sociaux). Pour les photos de foule d'événements : information claire sur place et possibilité de refuser. |
| Destinataires | Public ; Meta (Instagram). Meta est responsable de sa plateforme, et vous êtes en **responsabilité conjointe** avec Meta pour les statistiques de la page (jurisprudence de la CJUE sur les pages Facebook). |
| Contrat art. 28 | Sans objet pour Meta (conditions « Page Insights Controller Addendum ») |
| Transferts hors EEE | Oui, par nature (publication publique, Meta aux États-Unis) |
| Conservation | Jusqu'au retrait du consentement. Archives internes : **[proposition : tri annuel]**. |
| Sécurité | À mettre en place [proposition] : photos sur un stockage de l'entreprise, pas sur les téléphones personnels |
| Vigilance | Retrait du consentement = retirer le post. **Prudence renforcée pour les enfants sur Instagram** : privilégier des photos non identifiables (de dos, de loin). |

### 11. Site web WordPress

| Rubrique | Contenu |
|---|---|
| Finalités | Présenter la salle, recevoir les inscriptions (voir fiche 1), mesurer l'audience (?) |
| Personnes concernées | Visiteurs du site |
| Données | Adresse IP, journaux du serveur, cookies (lesquels ?) |
| Source | Navigation |
| Base légale proposée | Cookies techniques : aucun consentement requis. Cookies de mesure d'audience ou marketing (Google Analytics, pixel Meta) : **consentement préalable** via une bannière. |
| Destinataires | Hébergeur, outils tiers intégrés |
| Contrat art. 28 | Hébergeur, outils d'analyse |
| Transferts hors EEE | Oui si Google Analytics, pixel Meta, reCAPTCHA ou Google Fonts chargé à distance |
| Conservation | Journaux : **[proposition : 6 mois]** ; cookies : **[durée à confirmer]** |
| Sécurité | À mettre en place [proposition] : mises à jour, sauvegardes, comptes administrateurs protégés |
| Vigilance | Politique de confidentialité et politique cookies à publier |

## Questions ouvertes

1. **(Fiche 2)** Avez-vous vraiment besoin de connaître le détail des problèmes cardiaques ? Une attestation de non-contre-indication réduirait fortement le risque. Que faites-vous concrètement d'un « oui » ?
2. **(Fiche 2)** Combien de temps garder les décharges ? Question à poser à votre assureur RC.
3. **(Fiche 5)** Le parking est-il clôturé et privé ? Un lieu ouvert (non délimité) ne peut en principe pas être filmé par un acteur privé. La caméra filme-t-elle la voie publique ?
4. **(Fiche 5)** Les images sont-elles enregistrées, et où (enregistreur local, cloud) ? Le son est-il capté ? La déclaration à la police a-t-elle été faite ?
5. **(Fiche 4)** Le personnel badge-t-il aussi ? Le système est-il intégré au logiciel de gestion ?
6. **(Fiche 6)** La newsletter contient-elle de la promotion ? Les ex-membres la reçoivent-ils encore ?
7. **(Fiche 8)** Le Google Sheets est-il sur un compte Google Workspace ou sur un Gmail personnel ?
8. **(Fiche 9)** Les stages sont-ils encadrés par des moniteurs externes ou des étudiants ? Où sont gardées les fiches médicales pendant et après le stage ?
9. **(Fiche 11)** Quels outils sont intégrés au site : analytics, pixel Meta, reCAPTCHA, extension de formulaire ? Le formulaire garde-t-il une copie des soumissions dans WordPress ?
10. **(Général)** Traitements non mentionnés qui existent peut-être : **registre des accidents ou incidents** sur les murs (données de santé), **entrées à la journée** et cartes 10 accès, **recrutement** (CV des candidats), **fournisseurs**, cours et moniteurs indépendants, application de réservation de créneaux. À ajouter au registre s'ils existent.
11. **(Fiche 3)** Utilisez-vous un prestataire de paiement (Mollie, Stripe…) en plus de la banque ?

## Actions recommandées

| Action | Pourquoi | Priorité |
|---|---|---|
| Mettre la vidéosurveillance en conformité : déclaration à la police, pictogrammes, registre des images, conservation d'1 mois maximum, information du personnel (CCT 68) | Loi spécifique, sanctions possibles, cas fréquent de plainte | **1 – immédiat** |
| Revoir la déclaration cardiaque (idéalement la remplacer par une attestation) et faire valider la décharge par un conseiller | Donnée de santé sans base art. 9 claire | **1 – immédiat** |
| Encadrer les fiches médicales des stages : consentement explicite, accès limité, destruction après le stage | Données de santé d'enfants | **1 – avant les prochains stages** |
| Séparer les autorisations photo par usage et fixer une règle pour les enfants sur Instagram | Consentement spécifique requis, retrait possible | 2 |
| Collecter et archiver les contrats de sous-traitance (art. 28) : logiciel de gestion, hébergeur web, Mailchimp, Google, secrétariat social, installateur des caméras, système de badge | Obligation du responsable du traitement | 2 |
| Documenter les transferts vers les États-Unis (Mailchimp, Google, Meta, outils du site) : certification Data Privacy Framework ou clauses contractuelles types | Transferts hors EEE à justifier | 2 |
| Rédiger ou mettre à jour la politique de confidentialité (site + formulaire) et l'information du personnel | Art. 13 ; existence et contenu actuels à vérifier | 2 |
| Ajouter l'opposition à la newsletter dans le formulaire d'inscription et vérifier le lien de désinscription | Condition du soft opt-in | 2 |
| Fixer et appliquer les durées de conservation (purge annuelle des ex-membres, historiques de badge, soumissions WordPress) | Minimisation ; durées actuelles non communiquées [à vérifier] | 3 |
| Documenter pourquoi un DPO et une AIPD ne sont pas nécessaires (ou le sont), notamment pour la vidéo, la santé et les enfants | Responsabilité (art. 5.2) | 3 |
| Mettre en place une procédure simple pour les demandes d'accès et d'effacement et pour les violations de données (notification à l'APD sous 72 h) | Obligations des art. 15-22 et 33 | 3 |
| Mesures de sécurité de base : double authentification sur tous les outils, comptes nominatifs, mises à jour de WordPress | Réduit le risque de fuite | 3 |

Pour la suite :
- **Votre part :** répondez aux questions ouvertes (surtout 1, 3 et 10) et je compléterai les fiches.
- **Format :** je peux aussi mettre le registre en tableur, une ligne par traitement, sur la structure du modèle de l'Autorité de protection des données.
- **Point le plus urgent :** faites valider les fiches 2, 5 et 9 par un spécialiste.
