# L'imprimante de tickets n'imprime plus : « Imprimante hors ligne (code P-12) »

**S'applique à :** CaisseFacile sur Windows, avec une imprimante de tickets branchée en USB. Le problème apparaît souvent après une mise à jour de Windows.

## Symptômes

- L'imprimante de tickets n'imprime plus rien.
- CaisseFacile affiche le message **« Imprimante hors ligne (code P-12) »**.
- L'imprimante semble fonctionner : elle est allumée, le câble est branché et son voyant est **vert**.
- Éteindre puis rallumer l'imprimante ne règle pas le problème.

## Cause

CaisseFacile garde en mémoire le **port de communication** de l'imprimante, par exemple COM3. Certaines mises à jour de Windows réinstallent le pilote USB de l'imprimante. Windows lui donne alors un autre port, par exemple COM5.

CaisseFacile continue d'envoyer les tickets vers l'ancien port, où l'imprimante n'est plus. Elle est donc considérée comme hors ligne, alors qu'elle fonctionne.

## Solution

1. **Vérifiez le branchement.** Le câble USB doit être bien enfoncé des deux côtés : côté imprimante et côté ordinateur.
2. **Regardez le voyant de l'imprimante.** Il doit être **vert**. S'il n'est pas vert, le problème est différent : passez à la section « Si le problème persiste ».
3. Dans CaisseFacile, ouvrez **Réglages > Périphériques > Imprimante**.
4. Notez le port sélectionné (par exemple COM3). Il pourra vous servir si vous devez contacter le support.
5. Cliquez sur **« Détecter automatiquement »**. CaisseFacile cherche l'imprimante et choisit le bon port.
   *Si vous connaissez déjà le nouveau port de l'imprimante, vous pouvez aussi le choisir directement dans la liste.*
6. Enregistrez les réglages, puis imprimez un ticket pour vérifier.
   **Résultat attendu :** le ticket sort et le message « code P-12 » disparaît.

> **Bon à savoir :** le problème peut revenir après une prochaine mise à jour de Windows. Il suffit alors de refaire les étapes 3 à 6.

## Si le problème persiste

Contactez le support CaisseFacile dans les cas suivants :

- « Détecter automatiquement » ne trouve pas l'imprimante ;
- le voyant de l'imprimante n'est pas vert (par exemple orange) ;
- le ticket de test ne sort toujours pas après le changement de port.

Pour aller plus vite, préparez :

- le message d'erreur exact et son code (P-12 ou autre) ;
- la couleur du voyant de l'imprimante ;
- le port sélectionné dans Réglages > Périphériques > Imprimante, avant et après votre essai ;
- la date de la dernière mise à jour Windows, si vous la connaissez.

Le technicien pourra vous demander un accès à distance à votre poste pour identifier le bon port.

---

## Mots-clés proposés

imprimante hors ligne, P-12, code P-12, imprimante tickets n'imprime plus, ticket de caisse ne sort pas, port COM, COM3, COM5, mise à jour Windows imprimante, détecter automatiquement imprimante, imprimante USB caisse

**Articles liés à prévoir :** « Configurer une imprimante de tickets dans CaisseFacile », « Autoriser une prise en main à distance par le support ».

## Données retirées du ticket

- Nom du client et de son commerce, adresse, numéro de client, adresse e-mail
- Prénom du technicien
- Adresse IP et nom du PC de caisse
- Numéro de ticket (#45120) et référence du bug interne (DEV-882)
- Remarques internes : outil de prise en main à distance utilisé, nombre de cas similaires ce mois-ci

---

J'ai présenté l'article comme un texte à publier. Trois points sont à vérifier avant publication :

- **Lier l'article au bug DEV-882.** DEV-882 vise à reconnaître l'imprimante par son identifiant plutôt que par son port. Quand la correction sera livrée, il faudra réviser l'article : le « Bon à savoir » et une partie de la cause ne seront plus vrais. Je n'ai pas annoncé ce correctif aux clients, car le ticket ne dit pas s'il est prévu ni quand.
- **Le bouton « Détecter automatiquement ».** Julien l'a testé chez un autre client, pas dans ce ticket-ci. Une confirmation rapide sur un second poste serait utile.
- **Ce que le ticket ne précise pas.** Il ne dit pas s'il faut cliquer sur « Enregistrer », ni s'il existe un bouton « Imprimer un ticket de test ». Il ne dit pas non plus comment le client peut trouver lui-même le nouveau port. Je n'ai donc pas inventé de procédure Windows pour ça : l'article renvoie vers le support. Si vous le souhaitez, ajustez les libellés de l'étape 6 pour qu'ils correspondent exactement à l'écran.
