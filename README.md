# Skills Claude pour l'entreprise

23 skills en français pour les services d'une entreprise : ressources humaines, finance, commercial, marketing, juridique, support client, direction et IT. Chaque skill apprend à Claude une façon de travailler précise (les étapes, le format du livrable, les limites à respecter) pour une tâche que ces services font chaque semaine.

Les skills sont pensés pour des PME et des services belges : ils tiennent compte du droit belge quand c'est utile (antidiscrimination, retards de paiement, NIS2, bien-être au travail), du bilinguisme et des usages locaux, tout en restant utilisables ailleurs.

[![Validation](https://github.com/warrox1993/skills-claude-entreprise/actions/workflows/validation.yml/badge.svg)](https://github.com/warrox1993/skills-claude-entreprise/actions/workflows/validation.yml)

## À qui ça sert

- Aux équipes qui utilisent déjà Claude (Claude.ai, Cowork ou Claude Code) et veulent des résultats constants, au bon format, sans réécrire leurs consignes à chaque conversation.
- Aux dirigeants de PME qui veulent voir concrètement ce que Claude peut prendre en charge dans chaque service, et où s'arrête son rôle.
- Aux personnes qui créent leurs propres skills et cherchent des exemples complets, testés et documentés.

## Les skills par service

Ressources humaines (`entreprise-rh`)
- `offre-emploi-inclusive` : rédige ou relit une offre d'emploi claire, inclusive et prudente au regard du droit belge de l'antidiscrimination.
- `grille-entretien-structure` : construit une grille d'entretien structuré avec questions, échelle de notation ancrée et questions à ne pas poser.
- `plan-accueil-nouvel-arrivant` : prépare un plan d'intégration daté, de J-10 aux objectifs à 90 jours, avec les formalités à vérifier.

Finance et comptabilité (`entreprise-finance`)
- `analyse-ecarts-budgetaires` : explique les écarts entre budget et réalisé dans une note d'une page pour la direction, chiffres recalculés.
- `relances-factures-impayees` : prépare trois relances graduées, avec les mentions de la loi du 2 août 2002 ou du Code de droit économique à faire vérifier.
- `synthese-tresorerie` : construit une prévision de trésorerie en deux scénarios, repère le point bas et propose des leviers.

Commercial (`entreprise-commercial`)
- `preparation-rendez-vous-client` : produit une fiche d'une page avant un rendez-vous (objectif, questions, objections, prochaine étape).
- `reponse-objection-client` : analyse une objection et propose une réponse orale et écrite honnêtes, sans manipulation.
- `proposition-commerciale` : structure une offre centrée sur le problème du client, avec périmètre, exclusions, prix et hypothèses.

Marketing et communication (`entreprise-marketing`)
- `calendrier-editorial` : planifie 4 à 12 semaines de contenus à partir des objectifs et des moyens réels de l'équipe.
- `post-linkedin-entreprise` : écrit un post LinkedIn sobre et factuel, en deux longueurs, avec la liste des faits à vérifier.
- `adaptation-fr-nl-en` : adapte un texte entre le français, le néerlandais et l'anglais en documentant les choix de traduction.

Juridique et conformité (`entreprise-juridique`)
- `premiere-lecture-contrat` : résume un contrat, repère les clauses à risque et prépare les questions pour le juriste.
- `registre-traitements-rgpd` : établit les fiches du registre des traitements (article 30 du RGPD) et liste les questions ouvertes.
- `autodiagnostic-nis2` : évalue si l'organisation est probablement concernée par NIS2 en Belgique et par quoi commencer.

Support client (`entreprise-support-client`)
- `reponse-reclamation-client` : répond à une réclamation de façon humaine et tenable, avec une note interne sur la cause.
- `article-base-connaissances` : transforme un ticket résolu en article d'aide anonymisé et réutilisable.

Direction et gestion de projet (`entreprise-direction`)
- `compte-rendu-reunion` : tire d'une transcription ou de notes les décisions, les actions (qui, quoi, quand) et les points ouverts.
- `note-de-decision` : compare des options sur des critères explicites et formule une recommandation argumentée.
- `rapport-avancement-hebdo` : rédige le point hebdomadaire d'un projet avec météo, écarts au plan et décisions attendues.

IT (`entreprise-it`)
- `procedure-incident` : rédige une procédure d'incident utilisable sous stress, notifications RGPD et NIS2 comprises.
- `revue-politique-mots-de-passe-mfa` : compare une politique de mots de passe aux recommandations actuelles et la réécrit.
- `documentation-script` : documente un script d'administration pour qu'un collègue puisse le reprendre, secrets retirés.

Chaque skill contient un dossier `exemples/` avec une demande fictive réaliste (`entree.md`) et la réponse que Claude a réellement produite avec le skill lors du test (`sortie-attendue.md`). Ces réponses ont ensuite été relues ligne à ligne : tout fait absent de la demande a été retiré ou marqué `[à confirmer]`, pour que l'exemple ne contienne rien d'inventé.

## Installation

### Claude Code

Ajoutez la marketplace, puis installez les services qui vous intéressent :

```
/plugin marketplace add warrox1993/skills-claude-entreprise
/plugin install entreprise-rh@skills-entreprise
/plugin install entreprise-finance@skills-entreprise
```

Les mêmes opérations existent en ligne de commande, pratique pour un script d'installation :

```
claude plugin marketplace add warrox1993/skills-claude-entreprise
claude plugin install entreprise-juridique@skills-entreprise
```

Plugins disponibles : `entreprise-rh`, `entreprise-finance`, `entreprise-commercial`, `entreprise-marketing`, `entreprise-juridique`, `entreprise-support-client`, `entreprise-direction`, `entreprise-it`.

Une fois installé, un skill se déclenche seul quand votre demande correspond à sa description. Vous pouvez aussi l'appeler directement, par exemple `/entreprise-rh:offre-emploi-inclusive`.

### Claude.ai et Cowork

1. Téléchargez le dépôt, puis construisez les archives : `python3 scripts/empaqueter.py` crée un fichier `.zip` par skill dans `dist/`. Chaque archive contient le dossier du skill à sa racine, comme le demande Claude.ai.
2. Vérifiez que l'option « Exécution de code et création de fichiers » est activée (Paramètres, Capacités ; pour Team et Enterprise, c'est un réglage de l'organisation).
3. Dans Claude.ai, ouvrez Personnaliser, puis Skills, cliquez sur « + », « Créer un skill », « Importer un skill », et choisissez l'archive.
4. Le skill est ensuite disponible dans vos conversations et dans Cowork. Les skills importés dans Claude.ai sont personnels : chaque membre d'une équipe les importe pour lui-même.

## Exemple

Demande envoyée à Claude Code, sans nommer le skill (extrait de `plugins/entreprise-direction/skills/compte-rendu-reunion/exemples/entree.md`) :

> Mets-moi ça au propre, c'est la réunion de ce matin (lundi 28 septembre 2026), comité de pilotage du déménagement de nos bureaux [...]
> - câblage réseau nouveau bâtiment : Samia a reçu 2 devis, 18 400 et 23 900 €. [...] Pas tranché.
> - Anne veut aussi une étude sur le vélo, qui ? personne n'a pris.
> - Luc a parlé du burn-out de Stéphanie, elle ne sera pas là pour le déménagement.

Claude déclenche `compte-rendu-reunion` et rend un compte rendu avec les décisions, un tableau des actions où l'étude vélo apparaît `[à attribuer]`, le choix du câblage dans les points ouverts, et il écarte l'information de santé concernant une collègue en le signalant à l'utilisateur. La réponse complète est dans `sortie-attendue.md`.

## Garde-fous communs

Tous les skills suivent les mêmes principes, écrits noir sur blanc dans chaque `SKILL.md` :

- Claude prépare, structure et signale ; il ne prend pas de décision juridique, RH, financière ou de sécurité à la place d'un professionnel, et le dit quand c'est nécessaire.
- Rien n'est inventé : un chiffre, un nom, une clause ou une référence manquante apparaît comme `[à compléter]` ou `[à vérifier]`.
- Les références légales sont données comme des pistes à vérifier, avec la source officielle quand elle existe (SPF Finances, SPF Économie, CCB, Autorité de protection des données, Unia).
- Les données personnelles sont réduites au strict nécessaire : anonymisation des tickets, agrégation des salaires, aucun secret recopié dans une documentation.
- Les incertitudes sont signalées au lieu d'être masquées.

Ces skills ne remplacent ni un avocat, ni un expert-comptable, ni un conseiller en prévention, ni un responsable de la sécurité de l'information. Vérifiez toujours un livrable avant de l'utiliser.

## Comment les skills sont vérifiés

- `scripts/valider.py` contrôle la marketplace, chaque `plugin.json` et chaque `SKILL.md` : frontmatter YAML valide, nom identique au dossier (64 caractères au plus, minuscules, chiffres et tirets, sans mot réservé), description de 1024 caractères au plus, sections obligatoires, exemples présents.
- La CI GitHub Actions (actions épinglées par SHA) lance ce script, puis `claude plugin validate --strict` sur la marketplace et sur chaque plugin, puis construit les archives Claude.ai.
- `scripts/tester-skill.sh` teste un skill en conditions réelles : il envoie `exemples/entree.md` à Claude Code en mode non interactif, avec les huit plugins chargés, et vérifie que le bon skill se déclenche seul. Les 23 skills ont été testés ainsi avant publication : les 23 se sont déclenchés seuls, sur la seule base de leur description, et leurs réponses suivent le format annoncé.

## Structure du dépôt

```
.claude-plugin/marketplace.json     marketplace (8 plugins)
plugins/<service>/
  .claude-plugin/plugin.json        manifeste du plugin
  skills/<skill>/SKILL.md           instructions du skill
  skills/<skill>/exemples/          entrée fictive et sortie obtenue
scripts/valider.py                  validation de structure
scripts/tester-skill.sh             test réel avec Claude Code
scripts/empaqueter.py               archives pour Claude.ai et Cowork
```

## Documentation de référence

- Skills dans Claude Code : https://code.claude.com/docs/en/skills
- Plugins, manifeste et marketplaces : https://code.claude.com/docs/en/plugins et https://code.claude.com/docs/en/plugin-marketplaces
- Format des Agent Skills (limites de `name` et `description`) : https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Bonnes pratiques de rédaction : https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Utiliser et importer des skills dans Claude.ai : https://support.claude.com/en/articles/12512180-use-skills-in-claude et https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

## Projet indépendant

Ce dépôt est un projet personnel et indépendant. Il n'est ni affilié à Anthropic, ni approuvé par Anthropic. Claude est une marque d'Anthropic. Toutes les entreprises et personnes citées dans les exemples sont fictives.

## Auteur

Jean-Baptiste Dhondt, développeur full stack et IA à Liège.
GitHub : https://github.com/warrox1993
LinkedIn : https://www.linkedin.com/in/jean-baptistedhondt

Suggestions et corrections bienvenues via les issues du dépôt.

## Licence

MIT. Vous pouvez réutiliser, adapter et redistribuer ces skills, y compris dans un cadre commercial, en conservant la mention de licence.
