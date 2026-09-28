# nettoyage.ps1

Chaque nuit, ce script déplace vers le NAS les scans de plus de 30 jours, vide le dossier temporaire de Windows, puis envoie un e-mail « Nettoyage OK » à Kevin.

> ⚠️ **À régler avant le départ de Kevin (fin octobre)**
> 1. **Le script peut effacer des scans sans les avoir archivés.** Si la copie vers le NAS échoue, le fichier est quand même supprimé du serveur. C'est ce qui arrivera le jour où le compte NAS de Kevin sera désactivé ou son mot de passe changé.
> 2. **Un mot de passe est écrit en clair** dans le script (compte NAS personnel de Kevin).
> 3. **L'e-mail dit toujours « OK »**, même en cas d'échec, et il part dans la boîte de Kevin. Après son départ, plus personne ne verra rien.
>
> **Ne désactivez pas les comptes de Kevin tant que le script n'est pas corrigé ou suspendu.**

---

## Rôle et contexte

- **Objectif :** éviter que le partage `D:\Partages\Scans` se remplisse, en déplaçant les vieux scans vers le NAS. Au passage, le script vide aussi `C:\Windows\Temp`.
- **Où :** sur le serveur de fichiers, dans `C:\Scripts\` (à confirmer, c'est là que se trouve le journal).
- **Quand :** tous les jours à 2h00, par le planificateur de tâches, sous le compte administrateur local.
- **Qui en dépend :** toute personne qui cherche un vieux scan. Après 30 jours, il n'est plus dans le partage mais sur `\\NAS01\archives\scans`.
- **Auteur :** Kevin, 2021. Il n'existe pas d'autre documentation connue.

## Fonctionnement

1. **Connexion au NAS.** `net use Z: \\NAS01\archives` avec le compte `NAS01\kevin` et son mot de passe écrit dans le script. La lettre Z: n'est plus utilisée ensuite, mais cette connexion sert quand même : c'est elle qui donne les droits sur NAS01 au compte administrateur local. Si on retire cette ligne sans autre solution, la copie ne fonctionne plus.
2. **Recherche des vieux scans.** Le script parcourt `D:\Partages\Scans` et tous ses sous-dossiers. Il retient les fichiers **modifiés** il y a plus de 30 jours (date de dernière modification, pas date de création).
3. **Pour chaque fichier retenu :**
   - Il calcule le dossier de destination `\\NAS01\archives\scans\<nom du dossier parent immédiat>`. **Seul le dernier niveau de dossier est gardé** : `Scans\ClientA\2023\x.pdf` part dans `archives\scans\2023\x.pdf`. L'arborescence est donc aplatie.
   - Il crée ce dossier s'il n'existe pas.
   - Il copie le fichier en **écrasant** un éventuel fichier du même nom (`-Force`).
   - Il **supprime** l'original, **même si la copie a échoué**.
   - Il écrit « deplace <chemin> » dans `C:\Scripts\nettoyage.log`, là encore même si la copie a échoué.
4. **Vidage de `C:\Windows\Temp`.** Tout le contenu est supprimé, quel que soit l'âge des fichiers. Les erreurs sont ignorées sans message, par exemple pour les fichiers en cours d'utilisation.
5. **Envoi de l'e-mail** « Nettoyage OK » à kevin@exemple-courtage.be, **quoi qu'il se soit passé** avant.

Le script ne vérifie rien et ne s'arrête sur aucune erreur.

## Prérequis

| Élément | Détail |
|---|---|
| Système | Windows Server avec PowerShell 5.1 (version à confirmer) |
| Compte d'exécution | Administrateur local du serveur de fichiers (via la tâche planifiée) |
| Accès au NAS | Compte `NAS01\kevin`, mot de passe en clair dans le script ([SECRET RETIRÉ]) |
| Chemin source | `D:\Partages\Scans` (local) |
| Chemin destination | `\\NAS01\archives\scans` (partage SMB) |
| Journal | `C:\Scripts\nettoyage.log`, qui doit être accessible en écriture |
| SMTP | `smtp.exemple-courtage.be`, envoi sans authentification ni chiffrement (à vérifier qu'il l'accepte encore) |
| Lettre Z: | Doit être libre dans la session de la tâche |

## Paramètres et configuration

Le script n'accepte aucun paramètre. Tout est écrit en dur au début du fichier.

| Nom | Type | Défaut | Effet |
|---|---|---|---|
| `$src` | Chemin | `D:\Partages\Scans` | Dossier dont on retire les vieux scans |
| `$arch` | Chemin UNC | `\\NAS01\archives\scans` | Destination de l'archive |
| `$log` | Chemin | `C:\Scripts\nettoyage.log` | Journal des déplacements (grossit sans limite depuis 2021) |
| `$limite` | Date | Aujourd'hui − 30 jours | Âge minimum (date de modification) pour archiver |
| Identifiants NAS | Texte | `NAS01\kevin` / [SECRET RETIRÉ] | Accès au NAS |
| Destinataire e-mail | Texte | kevin@exemple-courtage.be | Seule personne prévenue |

## Effets et actions sensibles

- **Suppression définitive** des fichiers du partage Scans. Ils ne passent pas par la corbeille.
- **Écrasement silencieux** dans l'archive : deux scans qui portent le même nom et viennent de dossiers dont le dernier niveau a le même nom (par exemple deux dossiers `2023` différents) s'écrasent l'un l'autre. Seul le dernier copié reste.
- **Suppression de tout `C:\Windows\Temp`**, y compris des fichiers récents. À 2h du matin, cela peut perturber une mise à jour ou une installation en cours. Le risque est faible mais réel.
- **Noms de fichiers contenant des crochets `[ ]`** : sans `-LiteralPath`, PowerShell interprète ces crochets comme un motif de recherche. La copie et la suppression peuvent alors viser un autre fichier que prévu. Je n'ai pas pu vérifier le comportement exact sans tester, donc à traiter comme un risque.

## Exécution

**Planifiée :** planificateur de tâches, tous les jours à 2h00, compte administrateur local. Pour retrouver la tâche et son dernier résultat :

```powershell
Get-ScheduledTask | Where-Object { $_.Actions.Arguments -like '*nettoyage*' } |
  ForEach-Object { $_ ; $_ | Get-ScheduledTaskInfo }
```

Le code de retour vaudra probablement 0 même en cas d'échec, puisque le script ne signale aucune erreur. Il ne prouve donc rien.

**Manuelle :** ne pas lancer le script tel quel pour « voir ». Il supprime des fichiers.

**Tester sans rien changer** : cette commande liste ce qui *serait* déplacé, en lecture seule :

```powershell
$limite = (Get-Date).AddDays(-30)
Get-ChildItem 'D:\Partages\Scans' -Recurse -File |
  Where-Object { $_.LastWriteTime -lt $limite } |
  Select-Object FullName, LastWriteTime,
    @{n='Destination';e={ Join-Path '\\NAS01\archives\scans' $_.Directory.Name }}
```

**Vérifier que ça a marché**, le lendemain matin :
1. Dernières lignes du journal : `Get-Content C:\Scripts\nettoyage.log -Tail 20`
2. Pour quelques fichiers cités dans le journal, vérifier qu'ils existent **vraiment** dans `\\NAS01\archives\scans\...`. Le journal ne le garantit pas.
3. Ne pas se fier à l'e-mail « Nettoyage OK ».

## Dépannage

| Symptôme | Cause probable | Que faire |
|---|---|---|
| Des scans ont disparu du partage et sont introuvables sur le NAS | La copie a échoué (NAS inaccessible, compte Kevin désactivé, mot de passe changé, NAS plein) mais la suppression a eu lieu | Suspendre la tâche immédiatement, puis voir « Retour arrière » |
| Un scan archivé a un contenu différent de celui attendu | Écrasement par un fichier du même nom venant d'un autre dossier | Restaurer depuis la sauvegarde du NAS |
| Erreur « nom de périphérique local déjà utilisé » (erreur 85) | Z: déjà connecté dans la session | Sans gravité si la session vers NAS01 existe déjà. À supprimer dans la version corrigée |
| Erreur 1326 ou « accès refusé » sur le NAS | Mot de passe du compte `kevin` changé ou compte désactivé | **Danger de perte de données**, voir la première ligne du tableau |
| Plus d'e-mail reçu | Serveur SMTP qui exige maintenant une authentification, ou boîte de Kevin fermée | De toute façon, l'e-mail ne signalait pas les échecs |
| Journal très volumineux | Aucune rotation depuis 2021 | L'archiver, puis repartir d'un fichier vide |
| Partage Scans qui se remplit à nouveau | Tâche désactivée ou en échec | Vérifier la tâche, puis le journal |

## Retour arrière

- **Fichier supprimé de Scans mais présent sur le NAS** : le recopier depuis `\\NAS01\archives\scans\<dossier>` vers son emplacement d'origine. Le chemin exact d'origine se trouve dans le journal.
- **Fichier supprimé de Scans et absent du NAS** : le seul recours est la sauvegarde du serveur de fichiers, ou les clichés instantanés (Volume Shadow Copies) du lecteur D: s'ils sont activés : clic droit sur le dossier › Propriétés › Versions précédentes. À vérifier dès maintenant que l'un des deux existe.
- **Fichier écrasé dans l'archive** : sauvegarde ou instantanés du NAS01, si configurés.
- **`C:\Windows\Temp`** : pas de retour arrière. En principe, rien d'important ne doit s'y trouver.

## Risques relevés

| Risque | Gravité | Recommandation |
|---|---|---|
| Suppression de l'original même si la copie a échoué | **Haute** | Supprimer seulement après une copie vérifiée (arrêt sur erreur, contrôle de présence et de taille) |
| Mot de passe NAS en clair dans le script | **Haute** | Changer ce mot de passe (il est aussi dans ce message, et Kevin peut le réutiliser ailleurs). Utiliser un compte de service dédié, sans mot de passe dans le fichier |
| Dépendance au compte personnel de Kevin | **Haute** | Créer un compte de service NAS avec des droits limités au dossier `archives\scans` |
| Échecs invisibles : e-mail toujours « OK », envoyé à une personne qui part | **Haute** | Envoyer le rapport à une adresse partagée (ex. informatique@) et en indiquer le vrai résultat |
| Écrasement dans l'archive à cause de l'arborescence aplatie | Moyenne | Conserver le chemin relatif complet sous `archives\scans` |
| Exécution avec les droits administrateur local | Moyenne | Compte de service avec seulement les droits nécessaires |
| Chemins interprétés comme motifs (crochets) | Moyenne | Utiliser `-LiteralPath` |
| Vidage complet de `C:\Windows\Temp` | Faible | Limiter aux fichiers de plus de 7 jours, ou confier cette tâche à Windows (Assistant stockage / Nettoyage de disque) |
| Journal sans rotation, date au format dépendant de la langue du système | Faible | Un journal par mois, dates au format ISO |
| `Send-MailMessage` obsolète, sans chiffrement | Faible | Passer par le relais SMTP interne authentifié, ou un autre mécanisme d'alerte |

## En-tête à insérer dans le script

```powershell
<#
.SYNOPSIS
    Archive vers le NAS les scans de plus de 30 jours et vide C:\Windows\Temp.

.DESCRIPTION
    1. Ouvre une session SMB vers \\NAS01\archives (compte NAS01\kevin).
    2. Pour chaque fichier de D:\Partages\Scans (récursif) modifié il y a plus de 30 jours :
       copie vers \\NAS01\archives\scans\<dossier parent immédiat> (écrase si existant),
       puis SUPPRIME l'original, puis journalise dans C:\Scripts\nettoyage.log.
       ATTENTION : la suppression a lieu même si la copie échoue.
       ATTENTION : l'arborescence est aplatie (seul le dernier niveau de dossier est conservé).
    3. Supprime tout le contenu de C:\Windows\Temp (erreurs ignorées).
    4. Envoie "Nettoyage OK" par e-mail, sans condition de succès.

.NOTES
    Auteur        : Kevin, 2021. Documenté le 28/09/2026 pour passation.
    Exécution     : Planificateur de tâches, tous les jours à 02:00, administrateur local.
    Dépendances   : \\NAS01\archives, smtp.exemple-courtage.be, compte NAS01\kevin.
    Secret        : mot de passe NAS en clair plus bas. À RETIRER (voir documentation).
    Test sans effet : voir la documentation (commande de listage en lecture seule).
    Documentation : [emplacement de la doc interne]
#>
```

## Améliorations proposées

**Priorité 1, avant la désactivation des comptes de Kevin :**
1. Créer un compte de service sur le NAS, avec droits d'écriture limités à `archives\scans`.
2. Corriger la logique pour supprimer seulement après une copie vérifiée (`-ErrorAction Stop` + `try/catch`, puis contrôle de présence et de taille à la destination).
3. Retirer le mot de passe du script. Par exemple, faire tourner la tâche sous un compte de domaine qui a lui-même accès au NAS, ou utiliser le Gestionnaire d'identifiants Windows. Ensuite, changer le mot de passe de `NAS01\kevin`.
4. Envoyer le rapport à une adresse d'équipe, avec le vrai résultat : nombre de fichiers déplacés, nombre d'échecs.

**Priorité 2 :**
5. Conserver l'arborescence complète dans l'archive pour éviter les écrasements.
6. Utiliser `-LiteralPath` partout.
7. Ajouter un paramètre `-WhatIf` pour permettre les tests sans effet.

**Priorité 3 :**
8. Limiter le vidage de `C:\Windows\Temp` aux fichiers anciens, ou le retirer de ce script.
9. Mettre en place la rotation du journal et des dates au format ISO.
10. Vérifier qu'une sauvegarde couvre à la fois `D:\Partages\Scans` et `\\NAS01\archives`.

---

**Deux questions à poser à Kevin avant son départ :**
- Le compte `NAS01\kevin` sert-il ailleurs (autres scripts, sauvegardes, imprimantes/scanners qui déposent sur le NAS) ?
- Des scans ont-ils déjà disparu ou été écrasés depuis 2021 ?

Le nom du serveur, les chemins et les adresses sont des informations internes : à anonymiser si ce document doit sortir de l'entreprise. Je n'ai pas modifié le script. Je peux vous préparer une version corrigée qui traite la priorité 1.
