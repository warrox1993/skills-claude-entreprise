# Point hebdomadaire : dématérialisation des factures fournisseurs

**Semaine 39, du 21 au 25 septembre 2026**
**Destinataire :** directeur financier (sponsor)
**Auteur :** [à compléter]

## Météo

| Axe | Couleur | Justification |
|---|---|---|
| **Global** | **Rouge** | Le pilote du 05/10 ne peut pas démarrer sans votre validation de l'avenant de 6 000 €. |
| Délai | Rouge | Le jalon 1 a été atteint avec 5 jours de retard. La connexion ERP du 02/10 et le pilote dépendent d'une correction qui n'est pas encore lancée. |
| Budget | Orange | 51 000 € consommés sur 85 000 € (60 %). L'avenant de 6 000 € porterait le total engagé à 57 000 €. Il faut décider s'il rentre dans l'enveloppe ou s'il l'augmente (91 000 €). |
| Périmètre | Orange | L'outil ne lit pas encore les factures Peppol. Cette fonction est annoncée dans la version de novembre de l'éditeur, sans date précise. |
| Qualité | Orange | Le connecteur ERP fonctionne pour les factures simples. Les factures avec plusieurs taux de TVA sont rejetées. |

## Ce que nous attendons de vous

1. **Valider l'avenant de 6 000 €** pour le développement de la TVA multi-taux. Le travail est estimé à 4 jours. Pour tenir la connexion ERP au 02/10, il faut lancer la correction au plus tard le mardi 29/09. Chaque jour de retard dans la décision décale d'autant la connexion ERP et le pilote. Merci de préciser aussi si ce montant est pris sur les 85 000 € ou s'il s'y ajoute.
2. **Prendre connaissance du sujet Peppol**, qui touche à la conformité (voir « Risques et blocages »). Nous pouvons vous proposer des options la semaine prochaine [engagement à confirmer].

## Avancement par rapport au plan

| Jalon | Date prévue | Date prévue actualisée | Statut |
|---|---|---|---|
| 1. Paramétrage de l'outil de lecture automatique | 18/09 | 23/09 | Terminé avec 5 jours de retard (mise à jour livrée en retard par l'éditeur) |
| 2. Connexion avec l'ERP | 02/10 | 02/10 si l'avenant est validé le 29/09, sinon à redéfinir | Menacé : les factures multi-taux sont rejetées |
| 3. Pilote avec 3 fournisseurs | 05 au 23/10 | À confirmer après le jalon 2 | Bloqué sans l'avenant, et 1 fournisseur sur 3 n'a pas confirmé |
| 4. Généralisation | 16/11 | À confirmer | Dépend du pilote et de la version Peppol de novembre |

## Réalisé cette semaine

- Paramétrage de l'outil terminé le mercredi 23/09 (jalon 1).
- Connecteur ERP validé en test pour les factures à un seul taux de TVA.
- Anomalie sur les factures multi-taux identifiée et chiffrée par l'intégrateur : 4 jours de correction, 6 000 €.
- Fournisseurs pilotes choisis : Bureau Plus, Métallerie Ardennaise, Transport Loriot.
- Formation des 4 comptables planifiée le 01/10, salle réservée.

## Prévu la semaine prochaine (proposition à valider)

- Dès la validation de l'avenant, lancer la correction multi-taux chez l'intégrateur. Responsable : [à compléter]
- Relancer Transport Loriot et choisir un fournisseur de remplacement s'il n'a pas répondu d'ici [date à fixer]. Responsable : [à compléter]
- Vérifier si les 3 fournisseurs pilotes envoient déjà leurs factures en Peppol. Responsable : [à compléter]
- Donner la formation des 4 comptables le 01/10. Responsable : [à compléter]
- Demander à l'éditeur une date ferme pour la version de novembre (lecture Peppol). Responsable : [à compléter]
- Préparer des options pour traiter les factures Peppol d'ici là. Responsable : [à compléter]

## Risques et blocages

| Risque ou blocage | Impact | Action | Responsable | Échéance |
|---|---|---|---|---|
| Les factures avec plusieurs taux de TVA sont rejetées par le connecteur ERP | Pilote impossible, jalons 2 et 3 bloqués | Validation de l'avenant, puis 4 jours de correction | Sponsor, puis intégrateur | 29/09 |
| **Conformité :** la facturation électronique structurée entre entreprises est obligatoire en Belgique depuis le 01/01/2026. Certains fournisseurs envoient déjà en Peppol et l'outil ne sait pas lire ces factures. | Ces factures échappent au nouveau processus. Il faut vérifier comment elles sont reçues et traitées aujourd'hui. À terme, le projet risque d'automatiser surtout un flux papier/PDF qui diminue. | Faire l'état des lieux du traitement actuel des factures Peppol. Faire valider les obligations exactes par l'expert-comptable ou le conseiller fiscal. Obtenir une date ferme de l'éditeur. | [à compléter] | [à compléter] |
| La version Peppol de novembre n'a pas de date précise | La généralisation du 16/11 pourrait devoir attendre cette version | Obtenir un engagement de date de l'éditeur | [à compléter] | [à compléter] |
| Transport Loriot ne confirme pas sa participation au pilote | Pilote réduit à 2 fournisseurs ou démarrage retardé | Relance, avec un fournisseur de remplacement prêt | [à compléter] | [à compléter] |
| Retards de livraison de l'éditeur (5 jours sur le jalon 1) | Nouveaux glissements possibles sur les livraisons à venir | Suivi des dates de livraison au point hebdo avec l'éditeur | [à compléter] | Continu |

---

**Points à vérifier avant d'envoyer :**
- **Date du 29/09 :** je l'ai calculée ainsi : 4 jours de correction avant le 02/10. Faites-la confirmer par l'intégrateur. Elle ne compte pas le temps de retester après la correction, donc le 02/10 reste serré même si l'avenant est validé à temps.
- **Budget de 91 000 € :** je ne sais pas si l'avenant est prévu dans les 85 000 €, d'où la question posée au sponsor.
- **Règle Peppol :** je décris l'obligation belge dans ses grandes lignes. Faites confirmer son effet concret sur vos factures reçues par votre expert-comptable. Le rapport ne dit pas comment ces factures sont traitées aujourd'hui, et le sponsor posera probablement la question.
- **Champs à compléter :** l'auteur et les responsables sont à remplir.
