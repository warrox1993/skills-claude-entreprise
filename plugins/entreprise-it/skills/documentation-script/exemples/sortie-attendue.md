# nettoyage.ps1 : archivage des scans et purge du dossier temporaire

Chaque nuit, le script déplace vers le NAS les fichiers de `D:\Partages\Scans` qui n'ont pas été modifiés depuis plus de 30 jours. Il vide ensuite `C:\Windows\Temp` et envoie un e-mail « Nettoyage OK ».

> ⚠️ **Deux problèmes sont à traiter avant le départ de Kevin fin octobre.** Ils sont détaillés dans « Risques relevés ».
> 1. Si la copie vers le NAS échoue, **le fichier est quand même supprimé du serveur**. Il est alors perdu, sauf s'il existe une sauvegarde. Or le script se connecte au NAS avec le **compte personnel de Kevin**. Le jour où ce compte sera désactivé, chaque exécution risque de supprimer tous les scans de plus de 30 jours sans les archiver.
> 2. Le mot de passe de ce compte est écrit en clair dans le script.

---

## Rôle et contexte

- **But probable** : éviter que le partage des scans grossisse sans limite. Les documents scannés depuis plus d'un mois sont déplacés sur le NAS d'archives. Le nettoyage de `C:\Windows\Temp` a été ajouté au même script par commodité, sans lien avec les scans.
- **Serveur** : serveur de fichiers (nom à compléter).
- **Planification** : tâche planifiée tous les jours à 2h00, sous le compte administrateur local.
- **Auteur** : Kevin, 2021. Il n'y a aucune autre documentation connue.
- **Qui en dépend** : toute personne qui cherche un scan de plus de 30 jours. Ce scan ne se trouve plus sur `D:\Partages\Scans` mais sur `\\NAS01\archives\scans`. Les utilisateurs le savent-ils ?

## Fonctionnement

1. **Paramètres** : dossier source `D:\Partages\Scans`, destination `\\NAS01\archives\scans`, journal `C:\Scripts\nettoyage.log`, date limite = aujourd'hui moins 30 jours.
2. **Connexion au NAS** : `net use Z: \\NAS01\archives` avec le compte `NAS01\kevin` et son mot de passe [SECRET RETIRÉ].
   - Le lecteur `Z:` **n'est jamais utilisé ensuite**. Le script travaille avec le chemin réseau `\\NAS01\...`. Cette commande sert donc uniquement à ouvrir une session authentifiée sur le NAS. Sans elle, le compte administrateur local du serveur n'aurait sans doute pas le droit d'écrire sur le NAS.
   - Le lecteur n'est jamais déconnecté à la fin.
3. **Sélection des fichiers** : tous les fichiers de `D:\Partages\Scans` et de ses sous-dossiers dont la **date de dernière modification** (pas la date de création) a plus de 30 jours.
4. **Pour chaque fichier** :
   1. Le dossier de destination est `\\NAS01\archives\scans\<nom du dossier parent direct>`. **Seul le dernier niveau de dossier est conservé** : `Scans\ClientA\2024\scan001.pdf` arrive dans `archives\scans\2024\scan001.pdf`. Un fichier placé directement dans `Scans` arrive dans `archives\scans\Scans\`.
   2. Ce dossier est créé s'il n'existe pas.
   3. Le fichier est copié en **écrasant** un éventuel fichier de même nom (`-Force`).
   4. Le fichier source est **supprimé définitivement**, sans passer par la corbeille.
   5. Une ligne « <date> deplace <chemin complet> » est ajoutée au journal. Cette ligne est écrite **même si la copie a échoué**.
5. **Purge de `C:\Windows\Temp`** : tout son contenu est supprimé, quel que soit son âge. Les erreurs sont masquées (`-ErrorAction SilentlyContinue`), par exemple pour les fichiers en cours d'utilisation.
6. **E-mail** : un message « Nettoyage OK » part vers `kevin@exemple-courtage.be`. Il est envoyé **dans tous les cas**, même si tout a échoué. Il ne contient aucun détail (pas de corps, pas de nombre de fichiers).

## Prérequis

| Élément | Détail |
|---|---|
| Système | Windows Server avec PowerShell 3.0 ou plus (le paramètre `-File` de `Get-ChildItem` l'exige). |
| Compte d'exécution | Administrateur local du serveur. Il doit pouvoir lire et supprimer dans `D:\Partages\Scans`, supprimer dans `C:\Windows\Temp` et écrire dans `C:\Scripts`. |
| Compte NAS | `NAS01\kevin` : compte **personnel** local au NAS, avec droit d'écriture sur `\\NAS01\archives\scans`. |
| Réseau | Accès SMB (port 445) du serveur vers NAS01. Accès SMTP (port 25 par défaut, sans authentification ni chiffrement) vers `smtp.exemple-courtage.be`. |
| Lecteur | La lettre `Z:` doit être libre dans la session du compte d'exécution. |
| Fichiers | Le script est probablement dans `C:\Scripts\` (**à vérifier** dans la tâche planifiée). Le journal est `C:\Scripts\nettoyage.log`. |

## Paramètres et configuration

Aucun paramètre n'est passé au lancement. Tout est écrit en dur dans le script.

| Nom | Type | Défaut | Effet |
|---|---|---|---|
| `$src` | Chemin | `D:\Partages\Scans` | Dossier scanné récursivement. Ses fichiers anciens sont **supprimés**. |
| `$arch` | Chemin UNC | `\\NAS01\archives\scans` | Destination des archives. |
| `$log` | Chemin | `C:\Scripts\nettoyage.log` | Journal. Il grossit sans limite, sans rotation. |
| `$limite` | Date | Aujourd'hui − 30 jours | Âge minimal (date de modification) pour qu'un fichier soit déplacé. |
| Identifiants `net use` | Texte | `NAS01\kevin` / [SECRET RETIRÉ] | Authentification sur le NAS. |
| Destinataire du mail | Adresse | `kevin@exemple-courtage.be` | Seule notification existante. |
| Serveur SMTP | Nom d'hôte | `smtp.exemple-courtage.be` | Relais d'envoi. |

## Effets et actions sensibles

- **Suppression définitive** des fichiers source (étape 4.4), même si la copie a échoué. C'est l'action la plus dangereuse du script.
- **Écrasement** dans l'archive : deux fichiers de même nom venant de dossiers parents de même nom (par exemple `ClientA\2024\scan001.pdf` et `ClientB\2024\scan001.pdf`) se retrouvent au même endroit. Le second écrase le premier. Les scanners nomment souvent leurs fichiers `scan0001.pdf`, `doc00123.pdf`… Ce cas est donc plausible et **a peut-être déjà causé des pertes**.
- **Perte de l'arborescence** : l'archive ne garde que le dernier niveau de dossier.
- **Vidage complet de `C:\Windows\Temp`** : c'est en général sans conséquence la nuit. Cela peut toutefois gêner une installation ou une mise à jour Windows en cours à 2h00.
- **Journal trompeur** : « deplace » est écrit même si le fichier n'a pas été copié.
- **Alerte trompeuse** : « Nettoyage OK » est envoyé même en cas d'échec total.
- Les dossiers source vidés ne sont pas supprimés. L'archive, elle, n'est jamais purgée et grossit indéfiniment.

## Exécution

**Planifiée** : relever dans le Planificateur de tâches le nom exact de la tâche, la commande lancée (probablement `powershell.exe -ExecutionPolicy Bypass -File C:\Scripts\nettoyage.ps1`), l'option « exécuter même si l'utilisateur n'est pas connecté » et le compte utilisé. Reporter ces éléments ici.

**Manuelle** : à éviter tant que le problème de copie/suppression n'est pas corrigé. Si c'est nécessaire, lancer une console PowerShell en tant qu'administrateur puis `& C:\Scripts\nettoyage.ps1`.

**Test sans risque** (lecture seule, rien n'est modifié). Cette commande liste ce que le script déplacerait la prochaine nuit et signale les collisions de noms :

```powershell
$src = "D:\Partages\Scans"; $arch = "\\NAS01\archives\scans"
$limite = (Get-Date).AddDays(-30)
$liste = Get-ChildItem $src -Recurse -File | Where-Object { $_.LastWriteTime -lt $limite } |
    Select-Object FullName, LastWriteTime,
        @{n='Destination'; e={ Join-Path (Join-Path $arch $_.Directory.Name) $_.Name }}
$liste | Format-Table -AutoSize
# Fichiers qui s'écraseraient mutuellement dans l'archive :
$liste | Group-Object Destination | Where-Object Count -gt 1 | Select-Object Name, Count
```

Pour tester le script complet, en faire une copie. Ajouter `-WhatIf` à `New-Item`, `Copy-Item` et `Remove-Item`, puis mettre en commentaire la purge de `Temp` et l'envoi du mail.

**Vérifier que ça a marché** : l'e-mail ne prouve rien. Il faut contrôler :
- la fin de `C:\Scripts\nettoyage.log` (lignes datées de la nuit) ;
- la présence des fichiers correspondants sur `\\NAS01\archives\scans\` ;
- le « Résultat de la dernière exécution » de la tâche planifiée.

## Dépannage

| Symptôme | Cause probable | Que faire |
|---|---|---|
| Des scans ont disparu de `D:` et sont absents du NAS | La copie a échoué (NAS injoignable, compte refusé, disque plein) mais la suppression a eu lieu. | **Désactiver la tâche immédiatement.** Voir « Retour arrière ». |
| Un scan archivé a un contenu différent de celui attendu | Écrasement par un fichier de même nom venant d'un autre dossier. | Restaurer depuis une sauvegarde du NAS antérieure à la date d'archivage. |
| Erreur « nom de périphérique local déjà utilisé » (85) | `Z:` est déjà attribué dans la session du compte d'exécution. | `net use Z: /delete`, ou changer de méthode de connexion (voir améliorations). |
| Erreur 1219 « connexions multiples… avec des noms d'utilisateur différents » | Une connexion à NAS01 existe déjà avec un autre compte. | `net use \\NAS01\archives /delete`, puis relancer. |
| Erreur d'accès refusé / mot de passe incorrect sur le NAS | Le mot de passe du compte `kevin` a changé ou le compte a été désactivé. | **Désactiver la tâche** avant la prochaine nuit (risque de suppression sans copie). |
| Plus aucun e-mail reçu | Normal après le départ de Kevin : sa boîte n'existe plus. Ou alors le SMTP est injoignable. | Changer le destinataire. Ne pas considérer l'absence de mail comme une alerte fiable. |
| Le journal devient très volumineux | Aucune rotation. | Archiver ou tronquer `nettoyage.log` manuellement. |
| Fichiers au nom contenant `[` ou `]` jamais archivés | PowerShell interprète les crochets comme un motif (comportement à confirmer sur ce serveur). | Utiliser `-LiteralPath` (voir améliorations). |

## Retour arrière

Les fichiers supprimés **ne passent pas par la corbeille**. Sources possibles, dans l'ordre :

1. **L'archive NAS** : `\\NAS01\archives\scans\<dossier parent>\<nom>`. Le journal donne le chemin d'origine complet de chaque fichier, ce qui permet de reconstruire l'emplacement initial. Attention aux fichiers écrasés.
2. **Les clichés instantanés (VSS)** de `D:` s'ils sont activés : clic droit sur le dossier > Propriétés > Versions précédentes.
3. **La sauvegarde du serveur de fichiers et/ou du NAS** : vérifier qu'elle existe, ce qu'elle couvre et sa durée de rétention.

Il n'y a rien à restaurer pour `C:\Windows\Temp`.

## Risques relevés

| Risque | Gravité | Recommandation |
|---|---|---|
| Suppression du fichier source même si la copie a échoué | **Critique** | Ne supprimer qu'après une copie réussie et vérifiée. D'ici là, envisager de suspendre la tâche. |
| Dépendance au compte personnel `NAS01\kevin` : sa désactivation déclenchera le risque précédent | **Critique** | Créer un compte de service dédié sur le NAS **avant** de désactiver celui de Kevin. Ne pas désactiver le compte NAS de Kevin tant que le script n'est pas corrigé. |
| Mot de passe en clair dans le script (et désormais partagé dans cette conversation) | **Haute** | Considérer le mot de passe comme compromis et le changer. Stocker l'identifiant dans le Gestionnaire d'identifiants Windows ou un coffre de secrets. Il suit un schéma devinable (saison + année) : vérifier que ce schéma n'est pas réutilisé ailleurs. |
| Écrasement de fichiers de même nom dans l'archive, perte de l'arborescence | **Haute** | Reproduire le chemin relatif complet dans l'archive et ne jamais écraser. Vérifier dès maintenant si des pertes ont déjà eu lieu (commande de test ci-dessus). |
| Notification « OK » envoyée sans condition, vers une boîte qui va disparaître | **Haute** | Envoyer un résumé réel (fichiers traités, erreurs) à une adresse partagée (ex. `it@…`) et alerter en cas d'erreur. |
| Journal qui indique « deplace » même en cas d'échec | Moyenne | Journaliser le résultat réel de chaque opération. |
| Exécution sous l'administrateur local | Moyenne | Utiliser un compte de service aux droits limités (lecture/suppression sur `Scans`, écriture sur l'archive). |
| Vidage complet de `C:\Windows\Temp`, erreurs masquées | Faible | Ne supprimer que les éléments de plus de 7 jours, ou confier cette tâche à l'outil de nettoyage de Windows. |
| Archive jamais purgée, journal sans rotation | Faible | Définir une durée de conservation. Les scans d'un courtier contiennent probablement des données personnelles : la durée doit correspondre au registre RGPD. |
| `Send-MailMessage` déclaré obsolète par Microsoft, SMTP sans chiffrement | Faible | À remplacer lors d'une refonte. |

## En-tête à insérer dans le script

```powershell
<#
.SYNOPSIS
    Archive sur le NAS les scans de plus de 30 jours, puis vide C:\Windows\Temp.

.DESCRIPTION
    1. Se connecte à \\NAS01\archives (net use Z:, lecteur non utilisé ensuite ;
       sert uniquement à l'authentification).
    2. Pour chaque fichier de D:\Partages\Scans (récursif) dont la date de dernière
       modification a plus de 30 jours :
         - le copie vers \\NAS01\archives\scans\<dossier parent direct>\ (écrase si existant),
         - le SUPPRIME de la source (définitivement, même si la copie a échoué),
         - écrit une ligne dans C:\Scripts\nettoyage.log.
    3. Supprime tout le contenu de C:\Windows\Temp (erreurs ignorées).
    4. Envoie un e-mail "Nettoyage OK" (envoyé dans tous les cas).

    ATTENTION : si le NAS est injoignable ou refuse le compte, les fichiers sont
    supprimés sans être archivés. Voir la documentation avant toute modification
    du compte NAS utilisé.

.NOTES
    Auteur d'origine : Kevin (2021)
    Documenté le     : 2026-09-28
    Responsable      : [À COMPLÉTER]
    Planification    : Tâche planifiée "[NOM À COMPLÉTER]", tous les jours à 02:00,
                       compte administrateur local
    Dépendances      : NAS01 (SMB), smtp.exemple-courtage.be (port 25)
    Journal          : C:\Scripts\nettoyage.log
    Documentation    : [LIEN VERS CETTE DOCUMENTATION]
#>
```

## Améliorations proposées

Je n'ai rien modifié dans le script. Voici les corrections, par priorité :

1. **Maintenant, avant fin octobre** :
   - ne supprimer la source que si la copie a réussi : `-ErrorAction Stop` dans un `try/catch`, et idéalement comparer la taille ou le hash du fichier copié ;
   - créer un compte de service sur le NAS ;
   - changer le mot de passe exposé ;
   - rediriger le mail vers une adresse partagée.
2. **Retirer le mot de passe du script** : identifiant stocké via le Gestionnaire d'identifiants Windows ou un coffre de secrets, ou droits NAS accordés directement au compte de service sans `net use`.
3. **Conserver l'arborescence complète** dans l'archive et **refuser d'écraser** un fichier existant (le renommer ou le signaler).
4. **Journal et alerte honnêtes** : consigner succès et échecs, envoyer un résumé chiffré et signaler clairement les erreurs.
5. **Robustesse** : `-LiteralPath` pour les noms contenant des crochets, `net use /delete` en fin de script, rotation du journal, mode simulation (`-WhatIf` via `[CmdletBinding(SupportsShouldProcess)]`).
6. **Séparer la purge de `C:\Windows\Temp`** dans une tâche distincte, limitée aux fichiers anciens.
7. **Définir une durée de conservation** de l'archive, en cohérence avec le registre RGPD.

**Questions à poser à Kevin avant son départ** :
- Le compte `NAS01\kevin` sert-il à autre chose ?
- Y a-t-il une sauvegarde du NAS et de `D:` ?
- A-t-il déjà constaté des fichiers écrasés ou manquants ?
- Quel est le nom exact de la tâche planifiée ?
- D'autres scripts utilisent-ils le même compte ou le même mot de passe ?

Cette documentation contient des noms de serveurs, des chemins et des adresses internes. Elle doit rester interne ; si elle doit être publiée ailleurs, il faut d'abord anonymiser ces éléments. Je peux aussi écrire une version corrigée du script, qui traite au moins les points 1 et 3.
