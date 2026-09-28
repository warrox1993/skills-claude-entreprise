# Plan d'intégration de Sarah, développeuse back-end Java

## Résumé

- **Qui :** Sarah, développeuse back-end Java dans l'équipe produit (5 personnes). Son manager est Thomas, lead dev.
- **Quand :** elle commence le lundi 2 novembre 2026. Elle travaille sur site toute la première semaine, puis passe à 2 jours de télétravail par semaine à partir du 9 novembre.
- **Objectif à 90 jours (début février 2027) :** elle livre seule des user stories back-end de taille moyenne jusqu'en préproduction, en suivant les conventions de l'équipe, et elle participe aux revues de code et au support de l'équipe.

**Point d'attention :** le laptop a manqué la dernière fois. Il faut le commander **cette semaine**, le recevoir, puis le **tester par une vraie connexion avant le 30 octobre**. On garde aussi un poste de secours.

---

## Checklist avant l'arrivée

| Tâche | Responsable | Échéance | Fait |
|---|---|---|---|
| Désigner un parrain ou une marraine dans l'équipe (un dev confirmé, pas Thomas) et vérifier sa disponibilité en semaine 1 | Thomas | 2 oct. | ☐ |
| Commander le laptop (config dev : RAM suffisante pour IDE + Docker) et demander un délai de livraison ferme | Responsable IT | **2 oct.** | ☐ |
| Prévoir un **poste de secours** : un laptop de prêt déjà configuré, en cas de retard de livraison | Responsable IT | 16 oct. | ☐ |
| Vérifier le contrat signé et les formalités RH (voir « Formalités à confirmer ») | RH | 16 oct. | ☐ |
| Faire la déclaration Dimona | RH / secrétariat social | avant le 2 nov. (au plus tard le 30 oct.) | ☐ |
| Recevoir le laptop et l'inventorier (numéro de série, fiche de remise) | Responsable IT | 23 oct. | ☐ |
| Créer le compte Google Workspace (compte principal, en général utilisé pour se connecter aux autres outils) et l'activer au 2 nov. | Responsable IT | 26 oct. | ☐ |
| Créer ou préparer les comptes GitLab (groupes et projets de l'équipe produit), Jira (projet et board de l'équipe) et Slack (canaux de l'équipe, #general, canaux techniques) | Responsable IT + Thomas pour la liste des groupes et canaux | 28 oct. | ☐ |
| Préparer l'accès à la préproduction (VPN si nécessaire, droits minimaux au départ, élargis ensuite) | Responsable IT + Thomas | 28 oct. | ☐ |
| Installer le laptop : OS, chiffrement, gestionnaire de mots de passe, JDK et outils de build du projet, IDE, Docker, accès VPN | Responsable IT | 28 oct. | ☐ |
| **Tester le poste de bout en bout** : se connecter, cloner un dépôt, lancer le build, ouvrir Jira, accéder à la préprod | Responsable IT + parrain | **30 oct.** | ☐ |
| Mettre à jour le README et le guide « setup local » du projet principal (le parrain le suit lui-même pour vérifier qu'il fonctionne) | Parrain | 30 oct. | ☐ |
| Choisir un premier ticket « good first issue » : petit, réel, faisable en 1 à 2 jours | Thomas | 30 oct. | ☐ |
| Préparer le bureau, le badge ou les clés, l'écran, le clavier et la souris | Office manager / RH | 30 oct. | ☐ |
| Bloquer les rendez-vous de la semaine 1 dans les agendas (voir ci-dessous) | Thomas | 23 oct. | ☐ |
| Envoyer le message de bienvenue | Thomas | 23 oct. | ☐ |
| Annoncer l'arrivée de Sarah à l'équipe et à l'entreprise (message Slack le jour J) | Thomas | 2 nov. | ☐ |

---

## Jour 1 : lundi 2 novembre

| Heure | Activité | Avec qui |
|---|---|---|
| 9h00 | Accueil à l'entrée, café, présentation du programme de la semaine | Thomas |
| 9h30 | Remise du laptop, du badge et des accès. Première connexion et activation du MFA | Responsable IT |
| 10h30 | Volet RH : documents restants, règlement de travail, politique de télétravail, congés, notes de frais | RH |
| 11h15 | Visite des locaux et accueil sécurité (sorties de secours, premiers secours, personne de confiance, conseiller en prévention) | RH ou office manager |
| 12h00 | Déjeuner avec l'équipe produit [prise en charge à confirmer] | Équipe |
| 13h30 | Présentation du produit : à quoi il sert, pour qui, les grandes briques techniques | Thomas |
| 14h30 | Installation de l'environnement local en binôme, en suivant le guide setup | Parrain |
| 16h30 | Point de fin de journée : ce qui fonctionne, ce qui bloque | Thomas |

L'objectif du jour 1 : Sarah repart avec un poste qui fonctionne, le projet qui compile en local, et elle sait à qui poser ses questions.

---

## Semaine 1 (sur site)

- **Mardi 3 :** première participation aux rituels de l'équipe [daily ou autre, à confirmer]. Présentation de l'architecture back-end (services, base de données, CI/CD GitLab). Prise en main du premier ticket en binôme avec le parrain.
- **Mercredi 4 :** travail sur le premier ticket. Présentation des conventions : workflow Git, merge requests, revue de code, tests, Definition of Done. Rencontre de 30 minutes avec le Product Owner ou Product Manager [à compléter].
- **Jeudi 5 :** première merge request ouverte et revue par le parrain. Tour de la préprod : comment on y déploie, où lire les logs. Courte rencontre avec les interlocuteurs clés hors équipe (support, ops ou infra, QA) [rôles à compléter].
- **Vendredi 6 :** si possible, fusion du premier ticket. Point de fin de semaine avec Thomas (45 min). On fait le bilan de ce qui manque et on prépare le télétravail : matériel pour la maison, VPN testé depuis chez elle, disponibilités sur Slack.

**Semaine 2 :** le mercredi 11 novembre est un jour férié (Armistice). Il faut en tenir compte dans le planning et dans le choix des jours de télétravail.

---

## Objectifs 30 / 60 / 90 jours

| Étape | Objectif observable | Comment on le vérifie |
|---|---|---|
| **30 jours** (≈ 2 déc.) | Elle installe et fait tourner l'environnement complet sans aide | Elle a mis à jour elle-même le guide setup si besoin |
| | 3 à 5 tickets de petite taille livrés en préprod | Tickets Jira clôturés, MR fusionnées |
| | Elle connaît le workflow de l'équipe [rituels réels à préciser : daily, sprint, revue, déploiement ?] | Elle a participé à un cycle complet de l'équipe [sprint ou équivalent, à confirmer] |
| **60 jours** (≈ 8 janv. 2027, pause de fin d'année comprise) | Elle livre une user story de taille moyenne de bout en bout, avec les tests | Story livrée en préprod, peu d'allers-retours en revue |
| | Elle fait des revues de code utiles pour les autres | Au moins 5 revues avec commentaires constructifs |
| **90 jours** (≈ 1er févr. 2027) | Elle est autonome sur un périmètre fonctionnel défini [à compléter] | Elle estime et découpe les stories de ce périmètre en planning |
| | Elle traite un incident ou bug de préprod en suivant la procédure | Au moins un bug diagnostiqué et corrigé sans escalade |
| | Elle propose une amélioration (doc, outillage, dette technique) | Ticket ou MR proposé par elle |

À ajuster avec Thomas selon la roadmap réelle. La pause de fin d'année décale mécaniquement l'étape des 60 jours.

---

## Points de suivi

| Quand | Qui | Questions à poser |
|---|---|---|
| Chaque jour en semaine 1 (15 min, fin de journée) | Sarah + parrain | Qu'est-ce qui t'a bloquée ? Qu'est-ce qui manque dans la doc ? |
| Ven. 6 nov. | Sarah + Thomas | Tes accès et ton poste sont-ils complets ? Es-tu prête pour le télétravail ? Qu'est-ce qui t'a surprise ? |
| Hebdomadaire jusqu'au 90e jour (one-to-one, 30 min) | Sarah + Thomas | Où en sont les objectifs ? Charge de travail ? Qualité des retours en revue de code ? |
| ≈ 2 déc. (30 j) | Sarah + Thomas | Bilan des objectifs 30 j. Te sens-tu intégrée à l'équipe ? Le télétravail se passe-t-il bien ? |
| ≈ 8 janv. (60 j) | Sarah + Thomas | Bilan à 60 j. Sur quel périmètre veux-tu monter en compétence ? |
| ≈ 1er févr. (90 j) | Sarah + Thomas (+ RH) | Entretien de fin de période de démarrage : bilan, objectifs des 6 prochains mois |
| ≈ 1er févr. | Sarah + RH | **Retour sur l'accueil :** qu'est-ce qui a manqué ? Qu'est-ce qu'on doit garder ? Ces réponses servent à améliorer ce plan pour la prochaine personne. |

Le rôle du parrain : être disponible pour les questions, surtout les « petites » questions que personne n'ose poser. Il n'évalue pas Sarah.

---

## Formalités à confirmer

À faire valider par RH ou le secrétariat social. Cette liste n'est pas exhaustive : les obligations dépendent de la commission paritaire et du type de contrat.

- [ ] Déclaration **Dimona** faite avant le début des prestations
- [ ] Contrat de travail signé : type, date de début, commission paritaire applicable [à vérifier]
- [ ] **Règlement de travail** remis contre accusé de réception
- [ ] Assurance **accidents du travail** : couverture du nouveau travailleur, y compris en télétravail
- [ ] **Télétravail structurel** (2 jours par semaine) : convention ou avenant écrit selon la CCT n° 85 ou la politique interne. On y précise les jours, le matériel fourni, l'indemnité de bureau éventuelle et la joignabilité.
- [ ] **Accueil des nouveaux travailleurs** (Code du bien-être au travail, art. I.2-15) : informer Sarah des risques, désigner un travailleur expérimenté pour l'accompagner (le parrain peut jouer ce rôle), et vérifier avec le service externe de prévention si une surveillance de santé est requise pour ce poste (travail sur écran)
- [ ] Charte informatique, clause de confidentialité et, le cas échéant, clause de propriété intellectuelle sur le code
- [ ] Informations RGPD sur le traitement de ses données personnelles
- [ ] Données pour la paie : compte bancaire, frais de déplacement domicile-travail, avantages éventuels (chèques-repas, etc.)

---

## Message de bienvenue

À envoyer par Thomas vers le 23 octobre, sur l'adresse e-mail personnelle de Sarah.

> **Objet : Bienvenue chez [Entreprise], infos pratiques pour lundi 2 novembre**
>
> Bonjour Sarah,
>
> Toute l'équipe produit se réjouit de t'accueillir le lundi 2 novembre !
>
> **Pour ton premier jour :**
> - Rendez-vous à **9h00** au [adresse, étage, accès]. Je t'attendrai à l'accueil.
> - Parking / transports : [à compléter]
> - Pense à apporter ta carte d'identité et [documents demandés par RH, à compléter].
> - Le déjeuner est prévu avec l'équipe [prise en charge à confirmer avant envoi].
>
> **Ta première semaine** se passe entièrement sur site. Ce sera plus simple pour rencontrer tout le monde et bien démarrer. Le télétravail (2 jours par semaine) commence ensuite.
>
> Ton ordinateur et tes accès (Google Workspace, Slack, GitLab, Jira, préproduction) seront prêts à ton arrivée. [Prénom du parrain/de la marraine], développeur·se dans l'équipe, t'accompagnera pendant tes premières semaines pour tes questions, même les plus petites.
>
> Si tu as une question d'ici là, tu peux me joindre à cette adresse ou au [numéro].
>
> À très vite,
> Thomas

---

**À faire cette semaine :**
1. Commander le laptop. C'est la tâche la plus urgente.
2. Désigner le parrain ou la marraine.
3. Transmettre les éléments RH au secrétariat social.

Ce plan peut aussi servir de modèle pour les prochaines arrivées : il suffit de remplacer les noms et les dates. Si tu veux, je peux le mettre dans une page Notion pour que Thomas, l'IT et les RH cochent leurs tâches au même endroit.
