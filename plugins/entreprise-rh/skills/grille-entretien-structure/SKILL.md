---
name: grille-entretien-structure
description: "Construit une grille d'entretien d'embauche structuré (questions comportementales et situationnelles, critères observables, échelle de notation ancrée, questions à ne pas poser) à partir d'une offre ou d'une fiche de poste. À utiliser quand on prépare un entretien de recrutement, un jury de sélection, une trame de questions pour candidats, une scorecard ou quand on veut rendre les entretiens plus objectifs et comparables entre candidats."
---

# Grille d'entretien structuré

Les entretiens « au feeling » prédisent mal la réussite dans le poste et laissent passer les biais (affinité, premier impression, effet de halo). Un entretien structuré pose les mêmes questions à chaque candidat, relie chaque question à une compétence du poste et note les réponses sur une échelle définie à l'avance. Ce skill fournit cette grille, prête à imprimer.

## Informations à rassembler

- L'offre d'emploi ou la fiche de poste (missions, compétences)
- La durée prévue de l'entretien et le nombre d'intervenants
- Les compétences que l'entreprise juge décisives, si elle les connaît

Si seule une description vague est fournie, déduis 4 à 6 compétences et présente-les d'abord pour validation, en une phrase chacune.

## Démarche

1. **Choisir 4 à 6 compétences** vraiment liées au poste (techniques et comportementales). Plus de six dilue l'entretien.
2. **Écrire 1 à 2 questions par compétence** :
   - comportementale (« Racontez une situation où… ») pour ce qui a déjà été vécu ;
   - situationnelle (« Que feriez-vous si… ») pour ce que le candidat n'a peut-être jamais rencontré (profil junior, reconversion).
   Chaque question a 1 ou 2 relances neutres pour obtenir le contexte, l'action personnelle et le résultat.
3. **Définir une échelle ancrée de 1 à 4** pour chaque compétence, avec des indicateurs observables pour 1, 2-3 et 4. Une échelle paire évite le « moyen » par défaut.
4. **Lister ce qu'on ne demande pas.** En Belgique, les questions portant sur la vie privée sans lien avec le poste sont à proscrire, et celles qui touchent des critères protégés exposent l'entreprise : projet de grossesse ou d'enfants, situation familiale, état de santé ou handicap (sauf pour discuter d'un aménagement raisonnable si le candidat en parle), religion, opinions politiques ou syndicales, origine, âge. Adapte cette liste au poste.
5. **Prévoir le déroulé** minuté : accueil, présentation du poste, questions, questions du candidat, suite de la procédure.
6. **Préparer la fiche de synthèse** : chaque évaluateur note seul avant la discussion collective, pour éviter que la première opinion exprimée influence les autres.

## Format de sortie

Markdown, dans cet ordre :

1. `## Compétences évaluées` : tableau `Compétence | Pourquoi elle compte pour ce poste | Poids`
2. `## Déroulé` : liste minutée
3. `## Questions` : pour chaque compétence, un sous-titre, la ou les questions, les relances, puis l'échelle ancrée sous forme de tableau `Note | Indicateurs observables`
4. `## À ne pas demander` : puces, avec une reformulation acceptable quand elle existe (par exemple « Êtes-vous disponible pour une semaine de garde par mois ? » au lieu de questions sur la garde des enfants)
5. `## Fiche de notation` : tableau vierge `Compétence | Note (1-4) | Faits observés | Évaluateur`, suivi de la règle de consolidation (notes individuelles d'abord, discussion ensuite, décision argumentée par écrit)

## Garde-fous

- La grille aide à décider ; elle ne décide pas. La décision d'embauche reste celle des personnes responsables du recrutement.
- Ne propose ni test de personnalité ni question « piège » : ils sont peu fiables et mal vécus.
- Ne stocke ni ne réutilise de données sur des candidats réels. Si l'utilisateur colle un CV nominatif, travaille sur les compétences, pas sur la personne, et rappelle que les notes d'entretien sont des données personnelles (RGPD : accès du candidat, durée de conservation limitée).
- Si une compétence demandée paraît discriminatoire (« âge compatible avec l'équipe »), signale-le et propose un critère lié au travail réel.
- Principes communs : tu prépares et tu signales, la décision revient à la personne responsable ou au professionnel compétent (juriste, comptable, RH, sécurité) ; rien n'est inventé, ce qui manque est marqué `[à compléter]` et ce qui reste incertain `[à vérifier]` ; les références légales sont des pistes à vérifier auprès de la source officielle ; les données personnelles sont limitées au strict nécessaire.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
