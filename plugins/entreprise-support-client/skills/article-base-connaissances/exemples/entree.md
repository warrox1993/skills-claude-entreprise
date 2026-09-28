On a enfin résolu ce ticket, fais-en un article pour notre centre d'aide public (on édite un logiciel de caisse pour commerces, « CaisseFacile »).

---
Ticket #45120, ouvert le 14/09/2026 par Marc Dubois (Boulangerie Dubois, Rue Haute 8, Nivelles, client n° C-20931, marc.dubois@exemple.be)

Client : Depuis ce matin, l'imprimante de tickets ne sort plus rien. La caisse affiche « Imprimante hors ligne (code P-12) ». J'ai éteint et rallumé l'imprimante, rien.

Support (Julien) : Pouvez-vous vérifier que le câble USB est bien branché ? Et me dire si le voyant de l'imprimante est vert ou orange ?

Client : Câble ok, voyant vert.

Support (Julien) : Merci. Dans CaisseFacile, allez dans Réglages > Périphériques > Imprimante. Quel port est sélectionné ?

Client : COM3.

Note interne (Julien) : la mise à jour Windows de cette nuit a réinstallé le pilote USB-série et l'imprimante est passée de COM3 à COM5 sur son PC (vu via TeamViewer, IP 192.168.1.24, PC « CAISSE-01 »). Changé le port en COM5, test d'impression ok. Déjà vu 3 fois ce mois-ci chez d'autres clients après la même mise à jour. Le bouton « Détecter automatiquement » dans le même écran marche aussi, je l'ai testé chez un autre client. Bug ouvert chez les devs : DEV-882 (retenir l'imprimante par son identifiant plutôt que par le port).

Client : Ça remarche, merci !
---
