# Procédure rançongiciel, Cabinet de kinésithérapie, Mons

Version 1, septembre 2026, Responsable du document : Dr Maes
Prochaine relecture : [date à fixer, au moins une fois par an et après chaque incident]

> Ce document doit exister **sur papier** : un exemplaire au secrétariat, un chez le Dr Maes et un chez [suppléant·e]. Si les ordinateurs sont bloqués, la version informatique ne servira à rien.

---

## En cas d'incident : les 15 premières minutes

**Signes d'alerte :**
- un message à l'écran qui demande de payer ;
- des fichiers qui ne s'ouvrent plus ou dont le nom a changé (fin du nom inhabituelle, comme `.lock` ou `.crypt`) ;
- un fichier « LISEZ-MOI » ou « README » apparu dans les dossiers ;
- un ordinateur très lent sans raison ;
- un fond d'écran qui a changé.

**Au moindre doute, on applique la procédure. Une fausse alerte ne coûte rien, alors que 30 minutes de retard peuvent tout coûter.**

1. **Ne pas éteindre l'ordinateur.** Ne pas le redémarrer. Laisser l'écran tel quel.
2. **Débrancher le câble réseau** (le câble gris ou bleu à l'arrière de l'ordinateur) **et couper le Wi-Fi** (icône en bas à droite de l'écran, ou mode avion).
3. **Photographier l'écran avec un téléphone** (le message, le nom des fichiers). Noter l'heure.
4. **Aller au serveur** ([emplacement à compléter]) et **débrancher son câble réseau**, sans l'éteindre.
5. **Débrancher le disque USB de sauvegarde** du serveur et le ranger dans une enveloppe, à part. **Ne le rebrancher sur aucun ordinateur.**
6. **Faire le tour des autres ordinateurs.** Si l'un présente les mêmes signes, appliquer les étapes 1 à 3. Pour les autres, débrancher le câble réseau par précaution et ne plus s'en servir.
7. **Téléphoner au Dr Maes** (numéro sur la fiche contacts). Sans réponse après 10 minutes, appeler [suppléant·e].
8. **Téléphoner à la ligne d'urgence de l'assurance cyber** (numéro sur la fiche contacts). Vérifier sur la fiche contacts si elle est joignable le week-end [à vérifier]. Donner le numéro de la police d'assurance.
9. **Commencer le journal d'incident** (modèle en fin de document) : noter l'heure de chaque action.

**À NE PAS FAIRE**
- Ne pas payer, ne pas répondre aux pirates, ne pas cliquer sur leurs liens.
- Ne pas brancher de clé USB ni le disque de sauvegarde sur un ordinateur du cabinet.
- Ne pas se connecter au logiciel patients, à l'agenda ou à la messagerie **depuis un ordinateur du cabinet**. Si nécessaire, utiliser un téléphone ou un ordinateur personnel sain.
- Ne rien supprimer, ne rien « nettoyer », ne lancer aucune réinstallation.
- Ne rien dire aux patients, à la presse ou sur les réseaux sociaux avant l'accord du Dr Maes.

---

## Niveaux de gravité

| Niveau | Critères | Exemples | Délai de réaction | Qui décide |
|---|---|---|---|---|
| 1, Suspicion | Un seul poste au comportement anormal, aucun fichier chiffré | E-mail douteux ouvert, pièce jointe cliquée | Dans l'heure : isoler le poste, prévenir le Dr Maes. Le prestataire intervient le jour ouvrable suivant | Secrétaire, puis Dr Maes |
| 2, Poste touché | Fichiers chiffrés ou demande de rançon sur un poste, serveur apparemment intact | Message de rançon sur un seul PC | Immédiat : les 15 premières minutes au complet, assurance appelée le jour même | Dr Maes |
| 3, Cabinet touché | Serveur ou plusieurs postes chiffrés, ou disque USB touché | Comptabilité illisible | Immédiat, week-end compris | Dr Maes, avec l'assureur |
| 4, Données ou comptes en ligne touchés | Microsoft 365, logiciel patients ou agenda compromis, ou menace de publier des données | Les pirates disent avoir copié des données ; e-mails envoyés depuis un compte du cabinet à l'insu de son titulaire | Immédiat. Le délai de 72 h pour l'APD commence (voir Notifications) | Dr Maes, assureur, conseil juridique |

---

## Rôles

| Rôle | Titulaire | Suppléant | Responsabilités |
|---|---|---|---|
| Premier intervenant | Secrétaire présente | Toute personne présente | Applique les 15 premières minutes, tient le journal, prévient le Dr Maes et l'assurance |
| Décision | Dr Maes | [à désigner] | Déclare l'incident, décide des notifications, de la communication, de la reprise et de toute question liée à la rançon |
| Coordination | [à désigner, par ex. une secrétaire référente] | [à désigner] | Centralise les informations, tient le journal, organise l'accueil des patients sans informatique |
| Technique | Experts de l'assurance (si le contrat les prévoit [à vérifier]) | Prestataire habituel [nom], en semaine | Analyse, confinement, nettoyage, restauration |
| Communication | Dr Maes | [à désigner] | Messages au personnel, aux patients et aux partenaires |

---

## Déroulé

**1. Détection.** Tout le monde peut et doit signaler. On ne reproche jamais à quelqu'un d'avoir signalé ni d'avoir cliqué.

**2. Qualification** (Dr Maes, avec l'assurance) :
- Quels ordinateurs sont touchés ? Le serveur ? Le disque USB ?
- Microsoft 365 fonctionne-t-il normalement (tester depuis un téléphone) ? Des e-mails suspects partent-ils d'un compte du cabinet ?
- Le logiciel patients et l'agenda fonctionnent-ils (tester depuis un appareil sain) ?
- Les pirates parlent-ils d'un vol de données ?
- Choisir le niveau de gravité.

**3. Confinement.**
- Les postes et le serveur restent débranchés du réseau, sans être éteints, sauf consigne du technicien.
- **Sauvegarde cloud :** la copie du soir risque d'envoyer des fichiers chiffrés dans le cloud et d'écraser les bonnes versions. Débrancher le serveur l'empêche normalement. Le prestataire ou l'assurance doit vérifier au plus vite que la sauvegarde est suspendue et que les anciennes versions sont conservées.
- **Mots de passe :** sur consigne du technicien, les changer depuis un appareil sain pour Microsoft 365, le logiciel patients, l'agenda et la banque. Vérifier que la double authentification est activée.
- **Éditeur du logiciel patients :** le prévenir, même si le logiciel fonctionne, pour qu'il surveille les connexions venant du cabinet.
- Conserver le disque USB, les photos et le message de rançon : ce sont des preuves pour la police et l'assurance.

**4. Éradication** (technicien uniquement). Il identifie par où les pirates sont entrés, puis nettoie ou réinstalle les machines. Le personnel du cabinet n'intervient pas à cette étape.

**5. Restauration.**
- Uniquement après l'accord du technicien, sur des machines propres.
- Depuis une sauvegarde **vérifiée saine**, antérieure à l'infection.
- Faire contrôler les fichiers restaurés par la personne chargée de la comptabilité.
- Surveillance renforcée pendant [2 à 4 semaines].

**6. Clôture.** Le Dr Maes clôture l'incident quand les machines sont propres, les mots de passe changés, les notifications faites et le journal complet. Il fixe alors le retour d'expérience dans les deux semaines.

**Continuité des soins.** Le logiciel patients et l'agenda sont hébergés à l'extérieur : les consultations peuvent en général continuer, **uniquement depuis des appareils sains** et après accord du technicien. Prévoir un mode papier : liste des rendez-vous du jour (depuis l'agenda consulté sur téléphone) et cahier des séances à encoder plus tard. [À adapter : facturation, tiers payant, eHealth.]

---

## Notifications

Les délais sont des repères, à confirmer avec l'assureur et un conseil juridique.

| Destinataire | Quand | Délai | Qui | Condition |
|---|---|---|---|---|
| Dr Maes | Dès la découverte | Immédiat | Premier intervenant | Toujours |
| Assurance cyber | Dès la découverte | Immédiat. Le contrat fixe souvent un délai court [à vérifier] | Premier intervenant ou Dr Maes | Toujours. Suivre ses consignes, elle peut imposer ses experts |
| Prestataire habituel | Premier jour ouvrable, ou plus tôt s'il est joignable | Au plus vite | Dr Maes | Toujours, en accord avec l'assureur |
| Éditeur du logiciel patients | Dès la qualification | Le jour même | Dr Maes ou coordination | Toujours |
| Police locale (plainte) | Après les premiers gestes | Dans les jours qui suivent. Souvent exigée par l'assureur | Dr Maes | Recommandé. Apporter photos, journal et message de rançon |
| Autorité de protection des données (APD) | Si des données personnelles ont pu être lues, copiées, perdues ou rendues indisponibles | 72 h après en avoir pris connaissance (art. 33 RGPD) | Dr Maes (ou le DPO, s'il existe [à vérifier]) | Des données de santé sont probablement en jeu (factures, courriers sur le serveur). Partir du principe qu'il faut notifier, et le faire valider |
| Patients concernés | Si le risque pour eux est élevé | Dans les meilleurs délais (art. 34 RGPD) | Dr Maes | Sur décision, avec avis juridique |
| CCB (Centre pour la Cybersécurité Belgique) | Signalement volontaire | Au plus vite | Dr Maes ou technicien | Moins de 50 personnes : a priori pas concerné par NIS2 [à vérifier], mais le CCB accepte les signalements et peut aider |
| Banque | Si les accès bancaires ont pu être compromis | Immédiat | Dr Maes | Blocage préventif en cas de doute |

**La rançon.** Il est déconseillé de payer : cela ne garantit ni la récupération des fichiers ni la non-publication des données. Seul le Dr Maes décide, après avis de l'assureur, de la police et d'un conseil spécialisé. Personne d'autre ne contacte les attaquants.

---

## Communication

**Canal de secours** si la messagerie est touchée : [groupe WhatsApp, Signal ou SMS du cabinet, à créer dès maintenant].

**Message interne :**
> Un incident informatique touche le cabinet depuis [jour, heure]. Merci de **ne plus utiliser les ordinateurs du cabinet** jusqu'à nouvel ordre et de ne pas vous connecter au logiciel patients, à l'agenda ou à la messagerie depuis ces ordinateurs. Les consultations sont maintenues [ou : adaptées]. Notez vos séances sur papier. Merci de ne pas en parler aux patients ni sur les réseaux sociaux pour l'instant. Si vous avez remarqué quelque chose d'inhabituel ces derniers jours (e-mail étrange, pièce jointe), dites-le sans crainte. Prochain point : [heure]., Dr Maes

**Message d'attente aux patients** (après accord du Dr Maes) :
> Le cabinet rencontre actuellement un problème informatique. Les séances sont maintenues. Certains services (documents, factures, réponses par e-mail) peuvent prendre du retard. Merci de votre compréhension.

Ne parler ni de « piratage » ni de « vol de données » tant que ce n'est pas établi et validé.

---

## Journal d'incident

| Heure | Action | Par qui | Observation |
|---|---|---|---|
| *Exemple :* 08:42 | Message de rançon constaté sur le PC de l'accueil | [prénom] | Photo prise |
| | | | |
| | | | |
| | | | |

---

## Fiche contacts (à imprimer, sans aucun mot de passe)

| Qui | Nom | Téléphone | Disponibilité | Remarque |
|---|---|---|---|---|
| Gérant | Dr Maes | | | Décide |
| Suppléant·e | | | | |
| Assurance cyber, ligne d'urgence | | | [24/7 ? à vérifier] | N° de police : ……… |
| Courtier | | | | |
| Prestataire informatique | | | Semaine | |
| Éditeur du logiciel patients | | | | Réf. client : ……… |
| Agenda en ligne, support | | | | |
| Administrateur Microsoft 365 | | | | |
| Police locale (zone Mons-Quévy [à vérifier]) | | | | Urgence : 101 |
| APD | | | | Notification en ligne |
| CCB | | | | Formulaire sur son site |
| Banque, blocage | | | 24/7 | |
| DPO / conseil juridique | [à vérifier] | | | |

Emplacements : serveur [……] · mots de passe administrateur [coffre-fort ou enveloppe scellée chez ……] · police d'assurance papier [……] · accès à la sauvegarde cloud [……].

---

## Retour d'expérience (dans les 2 semaines, sans chercher de coupable)

- Comment l'incident a-t-il été détecté, et combien de temps après le début ?
- Les 15 premières minutes ont-elles pu être suivies ? Qu'est-ce qui était flou ?
- Les contacts ont-ils répondu ? Le numéro de l'assurance était-il le bon ?
- Les sauvegardes étaient-elles saines ? Combien de temps a pris la restauration ? Qu'a-t-on perdu ?
- Par où les pirates sont-ils entrés ? Qu'est-ce qui l'aurait empêché ?
- Les notifications ont-elles été faites dans les délais ?
- Que change-t-on, qui s'en charge et pour quand ?

---

## Points importants à régler dès maintenant

1. **Le disque USB branché en permanence ne protège pas vraiment.** Un rançongiciel chiffre généralement aussi les disques connectés. Demandez au prestataire d'alterner au moins deux disques, dont un toujours débranché et gardé hors du cabinet.
2. **Sauvegarde cloud.** Vérifiez qu'elle conserve plusieurs versions (par exemple 30 jours) et qu'une copie chiffrée ne remplace pas la bonne version. Sinon, l'étape 4 (débrancher le serveur) devient la seule chose qui sauve vos données.
3. **L'assurance cyber est votre vrai contact du samedi**, puisque le prestataire n'est joignable qu'en semaine. Lisez la police avec le courtier : numéro d'urgence, disponibilité le week-end, délai de déclaration, experts imposés, exclusions (certaines polices exigent la double authentification ou une sauvegarde hors ligne).
4. **Testez une restauration** deux fois par an, pendant la demi-journée du prestataire.
5. **Activez la double authentification** pour tout le monde sur Microsoft 365, le logiciel patients, l'agenda et la banque.
6. **Désignez les suppléants**, remplissez la fiche contacts et créez le groupe de messagerie de secours.
7. **Faites un exercice de 30 minutes avec les secrétaires :** lire la première page, puis trouver le serveur, son câble réseau et le disque USB.
8. Faites valider la partie RGPD (DPO éventuel, notification à l'APD) par un conseil juridique. Consultez aussi les guides du CCB pour les petites structures (Safeonweb@work).
