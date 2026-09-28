---
name: procedure-incident
description: "Rédige une procédure de gestion d'incident informatique ou de sécurité (runbook) utilisable sous stress : critères de déclenchement, niveaux de gravité, premiers gestes, qui prévenir et quand, confinement, communication, obligations de notification (RGPD, NIS2) à vérifier, retour à la normale et retour d'expérience. À utiliser dès qu'on parle de procédure d'incident, plan de réponse, runbook, rançongiciel, fuite de données, panne majeure, compromission de compte ou « que faire si… » côté IT."
---

# Procédure de gestion d'incident

Pendant un incident, personne ne lit un document de vingt pages. Une bonne procédure dit en une page quoi faire dans les quinze premières minutes, qui décide, qui prévenir et quelles erreurs éviter (éteindre une machine infectée et perdre les traces, payer une rançon sans avis, communiquer trop tôt). Ce skill produit cette procédure, adaptée à la taille et aux moyens réels de l'organisation.

## Informations à rassembler

- Le type d'incident visé (général, rançongiciel, fuite de données, compromission de messagerie, panne d'un service critique) ou toutes catégories
- La taille de l'organisation, l'équipe IT (interne, prestataire, astreinte ou non)
- Les systèmes critiques et les sauvegardes existantes
- Les contacts disponibles : prestataire, assureur cyber, DPO, direction, juriste
- Le cadre réglementaire applicable, s'il est connu (entité NIS2, traitement de données sensibles)

## Démarche

1. **Définir le déclenchement** : ce qui constitue un incident, et qui peut déclarer un incident (tout le monde doit pouvoir signaler, une personne désignée qualifie).
2. **Définir 3 ou 4 niveaux de gravité** avec des critères concrets (nombre d'utilisateurs touchés, données personnelles en jeu, arrêt de production) et le délai de réaction associé.
3. **Écrire les premiers gestes** sous forme de liste courte et ordonnée. Pour un incident de sécurité, les principes habituels : isoler du réseau plutôt qu'éteindre (pour préserver les traces), ne pas effacer ni réinstaller avant d'avoir conservé les éléments utiles, noter l'heure de chaque action, changer les accès compromis depuis un appareil sain.
4. **Fixer les rôles** : coordinateur de l'incident, technique, communication, décision (direction). Un rôle peut être tenu par la même personne dans une petite structure, mais il doit être nommé.
5. **Prévoir les notifications, à vérifier selon la situation** :
   - violation de données personnelles : notification à l'Autorité de protection des données dans les 72 heures après en avoir pris connaissance si la violation présente un risque (article 33 du RGPD), et information des personnes concernées si le risque est élevé (article 34) ;
   - entité soumise à NIS2 en Belgique : alerte précoce au CCB dans les 24 heures pour un incident significatif, notification dans les 72 heures, rapport final dans le mois ;
   - police (plainte), assureur cyber (souvent un délai contractuel court et une ligne d'urgence), clients selon les contrats.
6. **Préparer la communication** : interne (ce qu'on dit au personnel, canal de secours si la messagerie est touchée), externe (message d'attente validé par la direction).
7. **Décrire le retour à la normale** : restauration depuis des sauvegardes vérifiées, surveillance renforcée, critères de clôture.
8. **Prévoir le retour d'expérience** sous deux semaines, sans recherche de coupable.
9. **Ajouter une fiche contacts** à imprimer (car le réseau ou la messagerie peuvent être indisponibles).

## Format de sortie

Markdown :

1. `## En cas d'incident : les 15 premières minutes` : encadré court, liste numérotée, imprimable seul
2. `## Niveaux de gravité` : tableau `Niveau | Critères | Exemples | Délai de réaction | Qui décide`
3. `## Rôles` : tableau `Rôle | Titulaire | Suppléant | Responsabilités`
4. `## Déroulé` : détection, qualification, confinement, éradication, restauration, clôture
5. `## Notifications` : tableau `Destinataire | Quand | Délai | Qui notifie | Condition`
6. `## Communication` : messages types interne et externe
7. `## Journal d'incident` : modèle de tableau `Heure | Action | Par qui | Observation`
8. `## Fiche contacts` : modèle à compléter
9. `## Retour d'expérience` : questions à se poser

## Garde-fous

- Les délais légaux sont indiqués comme repères à vérifier : leur application dépend des faits et du statut de l'organisation. Recommande une validation par le DPO ou le juriste.
- Ne donne pas d'instructions techniques offensives. Pour un incident avancé (rançongiciel, intrusion), recommande de faire appel à un prestataire spécialisé en réponse à incident et, en Belgique, de consulter les ressources du CCB.
- Ne mets aucun mot de passe, clé ou secret dans la procédure : indique où ils sont conservés (coffre-fort de mots de passe, enveloppe scellée).
- Sur le paiement d'une rançon, ne recommande pas de payer ; renvoie la décision à la direction avec les autorités, l'assureur et un conseil spécialisé.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
