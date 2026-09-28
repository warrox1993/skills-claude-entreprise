# Autodiagnostic NIS2 : transformation de fruits, Saint-Trond

## Conclusion provisoire

**Avertissement :** ce diagnostic est indicatif. La qualification officielle et les obligations exactes se vérifient auprès du Centre pour la Cybersécurité Belgique (CCB), avec un juriste ou un consultant spécialisé.

**Vous êtes très probablement concernés, comme entité importante.** Confiance : **élevée**.

- **Votre activité est visée par la loi.** La loi belge du 26 avril 2024 (annexe II) vise la production et la transformation industrielles de denrées alimentaires. Confitures, compotes et sirops en font partie.
- **Votre taille dépasse les seuils.** Avec 78 équivalents temps plein, vous êtes une moyenne entreprise. Le seuil est de 50 personnes, et vos chiffres financiers le confirment.
- **Votre statut est « importante », pas « essentielle ».** Le secteur alimentaire est dans l'annexe II. Il donne le statut d'entité importante, que l'entreprise soit moyenne ou grande.

**Première urgence :** la date limite d'enregistrement était le 18 mars 2025 pour les entités qui existaient déjà. Si vous ne vous êtes pas enregistrés sur Safeonweb@work, c'est la première chose à faire.

## Analyse

| Critère | Votre situation | Effet sur la qualification |
|---|---|---|
| Secteur | Transformation industrielle de fruits en denrées alimentaires | Annexe II, « production, transformation et distribution de denrées alimentaires ». Rattachement clair |
| Effectif | 78 ETP | ≥ 50 : moyenne entreprise, donc dans le champ |
| Chiffre d'affaires / bilan | 19 M€ / 11 M€ | Au-dessus de 10 M€ chacun, sous les seuils « grande entreprise ». Confirme le statut de moyenne entreprise |
| Entreprises liées ou partenaires | Pas de filiale ni de maison mère | À confirmer (voir questions). Cela ne change rien ici, vous êtes déjà au-dessus des seuils |
| Établissement | Belgique | Loi belge, le CCB est l'autorité compétente |
| Situation cyber | Pas de référentiel, rançongiciel en 2023, automates de production, ERP externalisé | Sans effet sur la qualification, mais grand écart à combler |
| Clients | Grande distribution BE/NL, un peu de France | Le commerce de détail n'est pas visé par NIS2, mais ses exigences contractuelles vous touchent de toute façon |

## Obligations qui s'appliqueraient

1. **Enregistrement** auprès du CCB sur la plateforme Safeonweb@work.
2. **Mesures de gestion des risques** proportionnées, selon la liste minimale de l'article 21 :
   - analyse des risques ;
   - gestion des incidents ;
   - continuité d'activité, avec sauvegardes et reprise ;
   - sécurité de la chaîne d'approvisionnement. Votre prestataire qui héberge l'ERP est directement concerné ;
   - sécurité de l'acquisition et de la maintenance des systèmes ;
   - évaluation de l'efficacité des mesures ;
   - hygiène informatique et formation ;
   - cryptographie ;
   - sécurité du personnel et contrôle d'accès ;
   - authentification multifacteur.

   Le cadre de référence proposé par le CCB est **CyberFundamentals (CyFun)**. La norme ISO/IEC 27001 est aussi reconnue.
3. **Notification des incidents significatifs** au CCB, en trois étapes :
   - alerte précoce sous 24 heures ;
   - notification sous 72 heures ;
   - rapport final sous un mois.

   Un rançongiciel comme celui de 2023, qui arrête la production deux jours, serait très probablement un incident à notifier aujourd'hui.
4. **Responsabilité de la direction.** Le conseil d'administration et la direction approuvent les mesures et en surveillent la mise en œuvre. Ils doivent aussi suivre une formation.
5. **Supervision.** Pour une entité importante, le contrôle a lieu après coup, par exemple à la suite d'un incident ou d'une plainte. Une évaluation de conformité (CyFun ou ISO 27001) est volontaire, mais c'est le meilleur moyen de montrer votre conformité. Vérifiez les échéances et le régime des sanctions sur le site du CCB.

**Deux points propres à votre situation :**

- **Vos automates de production** doivent faire partie du périmètre. C'est souvent le point faible dans l'agroalimentaire, et c'est là que l'arrêt coûte le plus.
- **Le questionnaire de 60 questions** de votre client couvre en grande partie les mêmes sujets que CyFun. Une autoévaluation CyFun vous donne une base solide pour y répondre, et pour répondre aux questionnaires suivants.

## Plan de démarrage (90 jours)

| Action | Pourquoi | Échéance proposée | Responsable suggéré |
|---|---|---|---|
| Vérifier la qualification sur le site du CCB (outil de scoping) et, si elle est confirmée, s'enregistrer sur Safeonweb@work | Obligation légale, échéance initiale dépassée | Semaine 1–2 | Administrateur délégué + informaticien |
| Désigner un responsable cybersécurité et informer le conseil d'administration | La direction est responsable. Il faut un pilote interne | Semaine 2 | Conseil d'administration |
| Rédiger une procédure de notification d'incident (qui appelle le CCB, dans quels délais, sur quels critères) | Délais de 24 h et 72 h intenables sans procédure prête | Semaine 4 | Informaticien + direction |
| Faire l'autoévaluation CyFun, au niveau conseillé pour une entité importante | Mesurer l'écart et fixer les priorités | Semaine 4–8 | Informaticien, avec le prestataire |
| Faire le point avec le prestataire ERP : clauses de sécurité, sauvegardes, MFA, notification d'incident, réversibilité | Volet chaîne d'approvisionnement de l'article 21 | Semaine 6 | Direction + informaticien |
| Faire un inventaire de base des automates et du réseau de production (séparation du réseau bureautique, accès à distance de maintenance) | Risque d'arrêt de production, déjà vécu en 2023 | Semaine 8–10 | Informaticien + responsable production |
| Tester la restauration des sauvegardes (ERP et programmes des automates) | Continuité d'activité | Semaine 10 | Informaticien / prestataire |
| Organiser la formation de la direction et une première sensibilisation du personnel | Obligation de formation de la direction, et hameçonnage | Semaine 12 | Direction |
| Répondre au questionnaire du client à partir des résultats CyFun, et garder ces réponses comme base réutilisable | Enjeu commercial immédiat | Dès que CyFun est avancé | Informaticien + direction commerciale |

## Questions à clarifier

1. Êtes-vous déjà enregistrés sur Safeonweb@work, ou le CCB vous a-t-il contactés ?
2. L'actionnariat familial passe-t-il par une holding ou une société de patrimoine ? Cela ne change pas la conclusion, mais doit être noté dans le calcul de taille.
3. Faites-vous aussi du négoce en gros de fruits ou de produits finis ? Ce serait le même secteur et n'y changerait rien, mais à mentionner lors de l'enregistrement.
4. Le rançongiciel de 2023 a-t-il été complètement analysé (point d'entrée, mesures prises) ? C'est un bon point de départ pour l'analyse des risques.
5. Que prévoit le contrat avec le prestataire en matière de sécurité, de sauvegardes et de notification d'incident ?
6. Le client qui a envoyé le questionnaire a-t-il fixé une date de réponse ou un niveau attendu (CyFun, ISO 27001) ?

## Ressources officielles

- **Centre pour la Cybersécurité Belgique :** ccb.belgium.be, page NIS2 avec l'outil de vérification du champ d'application et la FAQ
- **Safeonweb@work :** plateforme d'enregistrement et de notification d'incident
- **CyberFundamentals :** cadre, outils d'autoévaluation et niveaux, sur le site du CCB

Vérifiez les dates, les seuils et le régime de sanctions sur ces sources officielles.

Je peux aussi rédiger la procédure de notification d'incident adaptée à votre situation (rançongiciel, arrêt des automates, délais NIS2). C'est une des actions les plus rapides à mettre en place.
