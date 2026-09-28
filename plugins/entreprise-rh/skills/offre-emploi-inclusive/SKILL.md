---
name: offre-emploi-inclusive
description: "Rédige ou relit une offre d'emploi claire, inclusive et compatible avec le droit belge de l'antidiscrimination (critères protégés, formulation neutre H/F/X, exigences justifiées). À utiliser dès qu'on demande d'écrire, corriger, moderniser ou vérifier une annonce de recrutement, une vacature, une job description ou une fiche de poste destinée à être publiée, même si le mot « inclusive » n'est pas prononcé."
---

# Offre d'emploi inclusive et conforme

Une offre d'emploi est souvent le premier contact entre l'entreprise et un futur collègue. Mal écrite, elle décourage de bons profils (exigences gonflées, jargon, formulations genrées) et peut exposer l'entreprise à une plainte pour discrimination. Ce skill produit une annonce lisible, honnête sur le poste et prudente sur le plan juridique.

## Informations à rassembler

Travaille avec ce que l'utilisateur fournit. S'il manque un élément essentiel (intitulé, missions principales, lieu, type de contrat), demande-le en une seule question groupée. Pour le reste, propose une valeur par défaut clairement marquée `[à compléter]` plutôt que d'inventer.

- Intitulé du poste, service, lieu de travail, possibilité de télétravail
- Missions concrètes (ce que la personne fera vraiment une semaine type)
- Compétences réellement indispensables et compétences appréciées
- Type de contrat, régime horaire, fourchette salariale et avantages si l'entreprise accepte de les publier
- Langues nécessaires et pourquoi (contact client néerlandophone, documentation en anglais, etc.)
- Procédure de candidature et calendrier

## Démarche

1. **Trier les exigences.** Sépare « indispensable » et « apprécié ». Une liste d'exigences trop longue écarte surtout les personnes qui ne cochent pas 100 % des cases, souvent des femmes et des profils atypiques. Vise 4 à 6 indispensables au maximum.
2. **Vérifier chaque exigence au regard des critères protégés.** En Belgique, la loi du 10 mai 2007 (antidiscrimination), la loi du 10 mai 2007 (genre) et la loi du 30 juillet 1981 (antiracisme), ainsi que les textes régionaux et communautaires, interdisent de distinguer sur des critères comme l'âge, le sexe et l'identité de genre, la nationalité ou l'origine, l'état de santé, le handicap, la conviction religieuse ou politique, l'orientation sexuelle, l'état civil, la fortune, la langue, la caractéristique physique ou l'origine ou condition sociale (liste non exhaustive ; depuis 2023, la loi vise aussi les critères supposés et la discrimination par association). Une exigence qui touche un de ces critères n'est admissible que si elle est objectivement justifiée par le poste. Exemples à signaler :
   - « jeune équipe dynamique », « 25-35 ans », « junior de moins de 30 ans » : critère d'âge implicite ou explicite ; remplace par le niveau d'expérience réellement attendu.
   - « langue maternelle néerlandaise » : remplace par un niveau de maîtrise (« très bonne maîtrise orale du néerlandais, niveau C1 »).
   - « permis B » alors que le poste ne suppose aucun déplacement : exigence non justifiée qui peut exclure certaines personnes handicapées.
   - « excellente présentation », « bonne condition physique » sans lien avec les tâches.
3. **Neutraliser la formulation.** Intitulé épicène ou suivi de « (H/F/X) », tournures neutres (« la personne recrutée », « vous »), pas de masculin générique dans les missions.
4. **Rendre l'annonce lisible.** Phrases courtes, verbes d'action, pas d'acronymes internes. Un candidat doit comprendre en 30 secondes ce qu'il fera, où, avec qui et à quelles conditions.
5. **Ajouter une mention d'ouverture sincère**, courte, et proposer d'indiquer comment demander un aménagement raisonnable pendant la sélection.
6. **Relire avec les yeux d'un candidat** : l'annonce est-elle honnête sur les contraintes (horaires, déplacements, charge) ? Une annonce trop belle produit des départs rapides.

## Format de sortie

Rends deux blocs, dans cet ordre :

1. **L'offre prête à publier**, en Markdown :
   - Titre du poste (H/F/X)
   - Deux ou trois phrases sur l'entreprise et l'équipe
   - « Votre rôle » : 4 à 7 puces
   - « Ce qui est indispensable » puis « Ce qui est un plus »
   - « Ce que nous offrons » (conditions, salaire si fourni, télétravail, formation)
   - « Comment postuler » (étapes, délais, contact pour un aménagement raisonnable)
   - Mention d'ouverture
2. **Le rapport de relecture**, sous forme de tableau : `Passage d'origine | Problème | Correction proposée | Niveau (à corriger / à vérifier / conseil)`. S'il n'y avait pas de texte d'origine, liste à la place les points que l'entreprise doit confirmer.

Termine par une ligne rappelant que la version finale doit être validée par la personne responsable RH ou un conseil juridique si un doute subsiste.

## Garde-fous

- Tu ne tranches pas la légalité d'une exigence : tu signales le risque (« peut constituer une discrimination, sauf justification objective ») et proposes une alternative, sans conclure qu'il y a discrimination. Les cas limites (exigence linguistique dans un service public, exigence physique pour un métier de sécurité, action positive) doivent être renvoyés vers le service juridique, un secrétariat social ou Unia.
- N'invente ni salaire, ni avantage, ni chiffre sur l'entreprise. Marque `[à compléter]` ce qui manque.
- Ne reprends aucune donnée personnelle d'un ancien titulaire du poste.
- Si l'utilisateur insiste pour garder une formulation discriminatoire, explique le risque une fois, clairement, sans moraliser, et laisse la décision à l'entreprise en le notant dans le rapport.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Le dossier `exemples/` contient une demande réaliste (`entree.md`) et le résultat attendu (`sortie-attendue.md`). Consulte-les si tu hésites sur le niveau de détail.
