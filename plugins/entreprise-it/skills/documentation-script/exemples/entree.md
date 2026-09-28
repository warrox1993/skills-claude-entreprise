Notre admin système part fin octobre. Il a laissé ce script qui tourne chaque nuit sur le serveur de fichiers, et personne ne sait vraiment ce qu'il fait. Documente-le pour son remplaçant.

```powershell
# nettoyage.ps1 - Kevin 2021
$src = "D:\Partages\Scans"
$arch = "\\NAS01\archives\scans"
$log = "C:\Scripts\nettoyage.log"
$limite = (Get-Date).AddDays(-30)

net use Z: \\NAS01\archives /user:NAS01\kevin Printemps2021!

Get-ChildItem $src -Recurse -File | Where-Object { $_.LastWriteTime -lt $limite } | ForEach-Object {
    $dest = Join-Path $arch $_.Directory.Name
    if (!(Test-Path $dest)) { New-Item -ItemType Directory -Path $dest | Out-Null }
    Copy-Item $_.FullName $dest -Force
    Remove-Item $_.FullName -Force
    Add-Content $log "$(Get-Date) deplace $($_.FullName)"
}

Get-ChildItem "C:\Windows\Temp" -Recurse | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Send-MailMessage -To "kevin@exemple-courtage.be" -From "serveur@exemple-courtage.be" -Subject "Nettoyage OK" -SmtpServer "smtp.exemple-courtage.be"
```

Il tourne via le planificateur de tâches tous les jours à 2h du matin, sous le compte administrateur local.
