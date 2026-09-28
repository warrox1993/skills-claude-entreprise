---
name: autodiagnostic-nis2
description: "Aide une organisation belge à faire un premier autodiagnostic NIS2 : est-elle probablement concernée (secteur, taille, cas particuliers), comme entité essentielle ou importante, quelles obligations en découlent (enregistrement, mesures de gestion des risques, notification d'incidents, responsabilité de la direction) et par quoi commencer, en renvoyant systématiquement vers le Centre pour la Cybersécurité Belgique (CCB) pour la qualification officielle. À utiliser dès qu'on parle de NIS2, de directive cybersécurité, de loi belge du 26 avril 2024, de CyberFundamentals, de Safeonweb@work ou qu'on se demande si l'entreprise doit se mettre en conformité."
---

# Autodiagnostic NIS2 (Belgique)

La directive NIS2 a été transposée en Belgique par la loi du 26 avril 2024 établissant un cadre pour la cybersécurité des réseaux et des systèmes d'information d'intérêt général pour la sécurité publique, en vigueur depuis le 18 octobre 2024. Beaucoup de dirigeants ne savent pas s'ils sont concernés. Ce skill fait un premier tri argumenté et oriente vers les bonnes ressources ; la qualification définitive relève de l'organisation elle-même, avec l'appui du CCB et de ses conseillers.

## Informations à rassembler

- Activité précise (pas seulement le code NACE), pays d'établissement
- Effectif (équivalents temps plein), chiffre d'affaires annuel et total du bilan, en tenant compte des entreprises liées ou partenaires
- Clients principaux (une organisation hors champ peut être fournisseur critique d'une entité concernée)
- Situation cyber actuelle : responsable désigné, référentiel utilisé (ISO 27001, CyberFundamentals), incidents passés

## Démarche

1. **Examiner le secteur.** La loi distingue des secteurs hautement critiques (annexe I : énergie, transports, secteur bancaire, infrastructures des marchés financiers, santé, eau potable, eaux usées, infrastructures numériques, gestion des services TIC entre entreprises, administration publique, espace) et d'autres secteurs critiques (annexe II : services postaux, gestion des déchets, fabrication et distribution de produits chimiques, production, transformation industrielles et distribution en gros de denrées alimentaires, le commerce de détail n'étant pas visé, fabrication de certains produits comme les dispositifs médicaux, équipements électroniques, machines et véhicules, fournisseurs numériques, recherche). Rapproche l'activité décrite des sous-secteurs, et dis quand le rattachement est incertain.
2. **Examiner la taille.** En règle générale, sont visées les moyennes et grandes entreprises au sens de la recommandation européenne 2003/361/CE (à partir de 50 personnes, ou plus de 10 millions d'euros de chiffre d'affaires annuel et plus de 10 millions d'euros de total du bilan, en comptant les entreprises liées et partenaires). Certaines entités sont concernées quelle que soit leur taille (par exemple certains fournisseurs de services DNS, registres de noms de domaine, prestataires de confiance, fournisseurs de réseaux ou services de communications électroniques publics, entités désignées par l'autorité).
3. **En déduire une qualification probable** : entité essentielle, entité importante, probablement hors champ, ou incertain. Explique le raisonnement en quelques lignes.
4. **Si l'entité est probablement concernée, lister les obligations principales** :
   - enregistrement auprès du CCB via la plateforme Safeonweb@work (l'échéance initiale était le 18 mars 2025 pour les entités existantes : si ce n'est pas fait, c'est la première action) ;
   - mesures de gestion des risques de cybersécurité proportionnées (l'article 21 de la directive en fixe la liste minimale : analyse des risques, gestion des incidents, continuité, chaîne d'approvisionnement, sécurité du développement, évaluation de l'efficacité, hygiène et formation, cryptographie, sécurité RH et contrôle d'accès, authentification multifacteur) ; le CCB propose le cadre CyberFundamentals (CyFun) et reconnaît aussi ISO/IEC 27001 ;
   - notification des incidents significatifs au CCB : alerte précoce dans les 24 heures, notification dans les 72 heures, rapport final dans le mois ;
   - responsabilité des organes de direction, qui approuvent les mesures, en supervisent la mise en œuvre et doivent suivre une formation ;
   - supervision et évaluation de conformité : pour les entités essentielles, évaluation périodique obligatoire (CyberFundamentals ou certification ISO/IEC 27001) avec des échéances échelonnées fixées par le CCB ; pour les entités importantes, supervision a posteriori et évaluation volontaire. Renvoie vers le CCB pour les dates applicables.
5. **Si l'entité est probablement hors champ**, dis-le prudemment et signale les cas où elle peut être indirectement touchée (exigences contractuelles de clients concernés, chaîne d'approvisionnement) ; propose une démarche volontaire légère.
6. **Proposer un plan de démarrage en 90 jours** : qualification confirmée, enregistrement, désignation d'un responsable, autoévaluation CyFun, procédure de notification d'incident, sensibilisation de la direction.

## Format de sortie

Markdown :

1. `## Conclusion provisoire` : qualification probable, niveau de confiance (élevé / moyen / faible) et pourquoi
2. `## Analyse` : tableau `Critère | Situation de l'organisation | Effet sur la qualification`
3. `## Obligations qui s'appliqueraient` (ou `## Pourquoi vous pourriez être concerné indirectement`)
4. `## Plan de démarrage` : tableau `Action | Pourquoi | Échéance proposée | Responsable suggéré`
5. `## Questions à clarifier`
6. `## Ressources officielles` : site du CCB (ccb.belgium.be), plateforme Safeonweb@work, cadre CyberFundamentals ; indique que les dates et seuils doivent y être vérifiés

## Garde-fous

- Ce diagnostic est indicatif. La qualification officielle et les obligations exactes doivent être vérifiées auprès du CCB, d'un juriste ou d'un consultant spécialisé ; dis-le en tête de la conclusion.
- Ne cite pas d'échéance ou de montant d'amende dont tu n'es pas sûr : renvoie à la source officielle.
- Ne demande pas d'information technique sensible (mots de passe, schémas réseau détaillés, vulnérabilités non corrigées) : l'autodiagnostic n'en a pas besoin.
- Si l'utilisateur décrit un incident en cours, arrête l'autodiagnostic et rappelle les délais de notification et les contacts d'urgence du CCB.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
