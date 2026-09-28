# Procédure rançongiciel : cabinet de kinésithérapie, Mons

Version 1, 28/09/2026. Responsable : Dr Maes.
**À imprimer en 3 exemplaires** : un à l'accueil, un dans le bureau du Dr Maes, un chez le Dr Maes. Si l'informatique est bloquée, seule la version papier sera disponible.

---

## En cas d'incident : les 15 premières minutes

**Signes d'alerte :**
- un message à l'écran demande de payer ;
- des fichiers ne s'ouvrent plus, ou leur nom se termine par une extension inconnue ;
- les icônes sont devenues blanches ;
- le fond d'écran a changé ;
- les documents du serveur (comptabilité, administratif) sont illisibles.

**Au moindre doute, appliquez cette procédure. Personne ne vous reprochera une fausse alerte.**

1. **N'éteignez pas l'ordinateur.** Ne le redémarrez pas, ne supprimez rien et ne cliquez pas dans le message.
2. **Débranchez le câble réseau** de l'ordinateur touché (câble avec l'étiquette rouge). **Coupez aussi le Wi-Fi** (icône en bas à droite > Wi-Fi désactivé).
3. **Débranchez le disque USB de sauvegarde** du serveur (étiquette « SAUVEGARDE »). Rangez-le dans le tiroir fermé de l'accueil avec un post-it « NE PAS REBRANCHER ». Ne le branchez sur aucun autre ordinateur.
4. **Débranchez le câble réseau du serveur** (étiquette rouge) mais laissez-le allumé. Cela bloque la copie cloud de ce soir, pour qu'elle n'écrase pas la bonne sauvegarde par des fichiers chiffrés.
5. **Photographiez l'écran** avec votre téléphone et notez l'heure.
6. **Prévenez à voix haute** les personnes présentes : « on n'utilise plus les ordinateurs du cabinet ». N'envoyez pas d'e-mail depuis un poste du cabinet.
7. **Appelez le Dr Maes.** S'il ne répond pas après 10 minutes, appelez son suppléant.
8. **Appelez la ligne d'urgence de l'assurance cyber** avec le numéro de police. Elle peut en principe envoyer un spécialiste même le week-end. **N'engagez aucune autre société sans son accord**, sinon les frais risquent de ne pas être remboursés.
9. **Commencez le journal d'incident** (modèle plus bas).

**Interdit :**
- payer ou répondre aux pirates ;
- réinstaller ou restaurer quoi que ce soit ;
- brancher le disque USB ailleurs ;
- se connecter à la messagerie ou au logiciel patients depuis un ordinateur du cabinet.

---

## Niveaux de gravité

| Niveau | Critères | Exemples | Délai de réaction | Qui décide |
|---|---|---|---|---|
| 1. Suspicion | Rien n'est bloqué, mais quelque chose est anormal | Clic sur un lien douteux, alerte antivirus | Le jour même : débrancher le poste, prévenir le Dr Maes, appeler le prestataire le jour ouvrable suivant | Secrétaire, puis Dr Maes |
| 2. Un poste touché | Un seul PC chiffré, le serveur fonctionne | Message de rançon sur le PC de l'accueil | Immédiat : les 15 premières minutes, puis l'assureur | Dr Maes |
| 3. Serveur ou plusieurs postes | Fichiers du serveur illisibles ou plusieurs PC touchés | Comptabilité inaccessible | Immédiat, et on arrête d'utiliser tous les ordinateurs | Dr Maes |
| 4. Données patients en jeu | Niveau 2 ou 3, avec en plus : les pirates disent avoir copié des données, ou il y a un accès suspect à la messagerie ou au logiciel patients | « Nous publierons vos données » | Immédiat. Déclaration à l'APD à préparer dans les 72 h | Dr Maes, avec l'assureur et le DPO |

En cas d'hésitation entre deux niveaux, choisissez le plus élevé.

---

## Rôles (à compléter)

| Rôle | Titulaire | Suppléant | Responsabilités |
|---|---|---|---|
| Premier intervenant | La secrétaire qui constate l'incident | Toute personne présente | Applique les 15 premières minutes, commence le journal, prévient le Dr Maes et l'assureur |
| Décision et coordination | Dr Maes | ………… (kiné désigné) | Fixe la gravité, décide des notifications, des dépenses et de la communication |
| Technique | Week-end : spécialiste de l'assureur. Semaine : ………… (prestataire) | Spécialiste de l'assureur | Analyse, confinement, nettoyage, restauration. Personne d'autre ne touche aux machines |
| Communication | Dr Maes | ………… | Messages au personnel, aux patients, à l'éditeur et aux autorités |
| Journal | Premier intervenant, puis une secrétaire désignée | ………… | Tient le journal papier et conserve les photos |

---

## Déroulé

**1. Détection.** Toute personne qui voit un signe d'alerte débranche le câble réseau de son poste et prévient l'accueil.

**2. Qualification (Dr Maes, par téléphone si besoin).**
- Combien de postes sont touchés ? Le serveur est-il touché ? Ne testez pas en ouvrant des fichiers depuis d'autres postes : demandez simplement aux collègues.
- Les pirates parlent-ils d'un vol de données ?
- Notez le niveau choisi dans le journal.

**3. Confinement.**
- Les postes touchés et le serveur restent allumés et débranchés du réseau.
- Si le spécialiste le demande, débranchez l'alimentation de la box internet (et du switch). Cela coupe tout le cabinet d'internet sans éteindre les ordinateurs.
- Microsoft 365, le logiciel patients et l'agenda sont hébergés à l'extérieur. Ils ne sont probablement pas chiffrés, mais les mots de passe tapés sur un poste infecté ont pu être volés. Le Dr Maes ou le prestataire s'en occupe **depuis un appareil sain** (téléphone personnel, PC à domicile) :
  - changer les mots de passe Microsoft 365 des comptes utilisés sur les postes touchés, en commençant par le compte administrateur, et vérifier que la double authentification (MFA) est active ;
  - appeler le support de l'éditeur du logiciel patients pour signaler l'incident, faire fermer les sessions ouvertes, vérifier les connexions récentes et changer les mots de passe ;
  - changer le mot de passe de l'agenda en ligne.

**4. Continuité des soins.**
- Les soins continuent.
- Consultez l'agenda depuis un téléphone en 4G, qui n'est pas connecté au Wi-Fi du cabinet.
- Notez les séances sur la fiche papier (patient, date, heure, kiné, type de séance) pour les encoder plus tard.

**5. Éradication (technicien uniquement).**
- Il cherche comment le virus est entré et s'il est encore présent.
- Aucune réinstallation avant que les traces utiles à l'assurance et à la police aient été conservées.

**6. Restauration (technicien, avec l'accord du Dr Maes).**
- Le disque USB, branché en permanence, a probablement été chiffré lui aussi. La copie cloud est sans doute la meilleure piste : il faut vérifier si elle garde plusieurs versions et depuis quand les fichiers sont chiffrés.
- On restaure sur une machine propre et on vérifie que les fichiers s'ouvrent avant de remettre en service.
- Les postes sont remis sur le réseau un par un, puis surveillés de près pendant 2 à 4 semaines.

**7. Rançon.** Le cabinet n'a pas l'intention de payer : payer ne garantit ni le retour des fichiers ni la non-publication des données. Si la question se pose quand même (aucune sauvegarde utilisable), le Dr Maes décide après avis de l'assureur, de la police et d'un conseil spécialisé. Personne ne contacte les pirates.

**8. Clôture.** L'incident est clos quand toutes ces conditions sont remplies :
- les machines sont déclarées saines ;
- les données sont restaurées et vérifiées ;
- les mots de passe sont changés ;
- les notifications sont faites ;
- les séances notées sur papier sont encodées.

---

## Notifications

Les délais sont des repères : **faites-les vérifier par le DPO ou un juriste** selon les faits. Les dossiers patients sont des données de santé : en cas de doute, considérez qu'il y a violation de données personnelles.

| Destinataire | Délai | Qui notifie | Condition |
|---|---|---|---|
| Assureur cyber (ligne d'urgence) | Immédiatement (délai contractuel à vérifier) | Premier intervenant, puis Dr Maes | Toujours, même en cas de doute |
| Prestataire informatique | Dès qu'il est joignable ; laisser un message le week-end | Dr Maes | Toujours |
| Éditeur du logiciel patients | Immédiatement | Dr Maes | Toujours, car les accès sont peut-être compromis |
| Police locale (zone Mons-Quévy) : plainte | Sous 24 à 48 h (souvent exigée par l'assureur) | Dr Maes | Toujours. Apporter les photos et le journal |
| Autorité de protection des données (APD) | **72 h** après en avoir pris connaissance (art. 33 RGPD), même avec des informations incomplètes | Dr Maes, avec le DPO | Sauf absence de risque pour les personnes, ce qui est rare avec des données de santé |
| Patients concernés | Dans les meilleurs délais | Dr Maes | Si le risque est élevé pour eux (art. 34 RGPD), par exemple un vol avéré de dossiers |
| CCB (Centre pour la Cybersécurité Belgique) | Pas de délai légal si le cabinet n'est pas soumis à NIS2 | Dr Maes ou prestataire | Probablement pas soumis (moins de 50 personnes), à confirmer. Une notification volontaire reste utile |
| Personnel | Dans l'heure | Dr Maes | Toujours |

---

## Communication

**Canal de secours :** la messagerie peut être compromise. Communiquez par téléphone et par le groupe WhatsApp ou Signal du cabinet, depuis les téléphones personnels.

**Message interne (Dr Maes) :**
> Incident informatique au cabinet ce [jour]. Merci de ne plus utiliser les ordinateurs du cabinet et de ne pas vous connecter à la messagerie ou au logiciel patients depuis ces postes, jusqu'à nouvel ordre. Les soins continuent : notez vos séances sur la fiche papier à l'accueil. N'en parlez pas aux patients ni sur les réseaux sociaux, renvoyez les questions vers moi. Prochain point : [heure].

**Réponse aux patients (secrétaires) :**
> Nous avons un problème informatique en cours de résolution. Votre rendez-vous est maintenu. Nous vous recontacterons si quelque chose change.

**Message externe (seulement si nécessaire, validé par le Dr Maes et l'assureur) :**
> Le cabinet a été victime d'un incident informatique le [date]. Nous avons immédiatement pris des mesures pour le contenir avec l'aide de spécialistes et informé les autorités compétentes. Les soins se poursuivent. Si des données vous concernant ont été touchées, nous vous en informerons directement. Contact : [...]

Ne donnez aucun détail technique et aucune hypothèse sur l'auteur.

---

## Journal d'incident (sur papier, imprimez-en 3 pages à l'avance)

Incident du ……/……/…… Niveau : …… Constaté par : ……………

| Heure | Action | Par qui | Observation |
|---|---|---|---|
| 08:42 | Message de rançon constaté sur le PC de l'accueil | (prénom) | Photo prise |
| 08:44 | Câble réseau du PC débranché, Wi-Fi coupé | | |
| 08:46 | Disque USB débranché et rangé | | |
| | | | |

---

## Fiche contacts (à compléter, plastifier et garder à côté du téléphone de l'accueil)

**Aucun mot de passe sur cette fiche.**

| Qui | Nom | Téléphone | Autre info | Disponibilité |
|---|---|---|---|---|
| Dr Maes | | | | |
| Suppléant | | | | |
| Assurance cyber : ligne d'urgence | | | N° de police : | 24 h/24 ? |
| Courtier d'assurance | | | | |
| Prestataire informatique | | | | En semaine |
| Support du logiciel patients | | | | |
| Agenda en ligne | | | | |
| Fournisseur internet | | | N° client : | |
| DPO / conseil RGPD | | | | |
| Police locale Mons-Quévy | | | | |
| APD | | | autoriteprotectiondonnees.be | |
| CCB | | | ccb.belgium.be / safeonweb.be | |

Les mots de passe administrateur sont conservés : ……………… (par exemple dans une enveloppe scellée au coffre du Dr Maes).

---

## Retour d'expérience (dans les deux semaines, sans chercher de coupable)

Participants : le Dr Maes, les secrétaires, le prestataire et un kiné. La personne qui a cliqué doit surtout entendre qu'elle a bien fait de signaler vite.

- Comment le virus est-il entré ? Qu'est-ce qui aurait pu l'arrêter ?
- Combien de temps s'est écoulé entre les premiers signes et la réaction ?
- Quelle étape de la procédure a posé problème aux secrétaires ?
- La sauvegarde était-elle utilisable ? Combien de jours de travail ont été perdus ?
- Les notifications ont-elles été faites à temps ?
- Que change-t-on, qui s'en charge et pour quand ?

---

## Annexe : à faire maintenant, avant tout incident

1. **Disque USB branché en permanence : c'est le point faible principal.** Le virus le chiffrera avec le serveur. Il faut passer à deux disques en alternance, dont un toujours débranché et rangé hors du cabinet.
2. **Copie cloud** : vérifier qu'elle garde plusieurs versions (au moins 30 jours) et que le serveur ne peut pas les effacer. Sinon, la sauvegarde de la nuit qui suit l'attaque remplacera les bonnes copies par des fichiers chiffrés.
3. **Tester une restauration** deux fois par an.
4. **Assurance cyber** : relire le contrat et noter sur la fiche contacts la ligne d'urgence, le délai de déclaration et les garanties. Vérifier aussi les exclusions : certains contrats exigent la MFA ou des sauvegardes hors ligne.
5. **Double authentification (MFA)** sur Microsoft 365 et sur le logiciel patients.
6. **Étiqueter en rouge** les câbles réseau et le disque USB, et montrer aux secrétaires où ils se trouvent.
7. **Désigner** le suppléant du Dr Maes et le DPO.
8. **Créer** le groupe WhatsApp ou Signal du cabinet et la fiche papier de séances.
9. **Exercice « samedi fictif »** de 30 minutes par an avec les secrétaires.
10. **Confirmer auprès du CCB** que le cabinet n'est pas soumis à NIS2.

---

**À savoir :**
- Tant que les étiquettes rouges ne sont pas posées et la fiche contacts remplie (surtout la ligne d'urgence de l'assureur), les secrétaires ne pourront pas appliquer la procédure un samedi.
- Le disque USB branché en permanence est le vrai risque. Le point 1 de l'annexe est à régler en priorité avec votre prestataire.
