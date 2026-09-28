---
name: article-base-connaissances
description: "Transforme un ticket de support résolu (échange avec le client, notes techniques, solution trouvée) en article de base de connaissances ou de FAQ réutilisable : titre formulé comme le client cherche, symptômes, cause, solution pas à pas, variantes, quand contacter le support, le tout anonymisé. À utiliser dès qu'on veut documenter une solution, créer un article d'aide, une FAQ, une procédure de dépannage pour les clients ou l'équipe support à partir d'un cas réel."
---

# Article de base de connaissances à partir d'un ticket résolu

Chaque ticket résolu contient une réponse que d'autres clients chercheront. Si elle reste enfouie dans l'outil de support, l'équipe la redécouvre à chaque fois. Ce skill en fait un article clair, trouvable et sans données personnelles.

## Informations à rassembler

- Le fil du ticket (messages, notes internes) et la solution finalement appliquée
- Le public de l'article : clients (article public) ou équipe support (article interne)
- Le produit, la version ou le contexte concerné
- Les captures ou messages d'erreur exacts, s'il y en a

## Démarche

1. **Anonymiser d'abord.** Retire noms, e-mails, numéros de client, adresses, identifiants techniques propres au client (adresse IP, nom de machine). Remplace-les par des éléments génériques. Si un détail personnel est indispensable pour comprendre, décris-le de manière générique.
2. **Trouver le titre que le client taperait** : le symptôme, dans ses mots (« Le lecteur de badges affiche "Erreur 403" au démarrage »), pas le nom interne de la cause.
3. **Séparer symptôme, cause et solution.** Le client lit le symptôme pour savoir s'il est au bon endroit, la solution pour agir, la cause pour comprendre (et éviter que ça revienne).
4. **Écrire la solution en étapes numérotées**, une action par étape, avec le résultat attendu quand c'est utile (« Le voyant passe au vert »). Commence par les vérifications les plus simples et sans risque.
5. **Signaler les variantes** : autres versions, autres systèmes, cas où la solution ne s'applique pas.
6. **Dire quand arrêter** : à partir de quel point le client doit contacter le support, et quelles informations préparer pour gagner du temps.
7. **Distinguer public et interne** : un article public ne contient ni contournement risqué, ni accès administrateur, ni détail de sécurité exploitable. Si le ticket en contient, mets-les dans une section interne séparée.
8. **Proposer des mots-clés** et des articles liés.

## Format de sortie

Markdown :

1. `# [Titre formulé comme le symptôme]`
2. `**S'applique à :**` produit, versions, contexte
3. `## Symptômes`
4. `## Cause`
5. `## Solution` : étapes numérotées
6. `## Si le problème persiste` : quand et comment contacter le support, informations à fournir
7. `## Notes internes` : seulement si l'article est interne ou si des éléments doivent rester internes
8. Hors article : `## Mots-clés proposés` et `## Données retirées du ticket` (liste des types d'informations anonymisées, pour contrôle)

## Garde-fous

- Aucune donnée personnelle du client dans l'article, même partielle.
- N'invente pas d'étape que le ticket ne contient pas. Si la solution a été trouvée par tâtonnement, garde seulement ce qui a fonctionné et signale ce qui reste à confirmer par un technicien.
- N'expose pas de faille de sécurité non corrigée ou de procédure qui contourne une protection dans un article public.
- Si la solution relève d'un bug du produit, recommande de lier l'article au ticket de correction et de le réviser quand le correctif sort.

## Exemple

Voir `exemples/entree.md` et `exemples/sortie-attendue.md`.
