# Fiche RDV : Transports Delvaux (Ans), demain 10h, 1h

## Objectif et prochaine étape visée
**Objectif :** vérifier que le départ en retraite de mars et les pénalités de la grande distribution posent un vrai problème chiffrable, et que notre outil peut se brancher sur leur TMS.
**Prochaine étape visée :** un atelier de cadrage de 2h **avant le 16 octobre**, avec le responsable IT et le dispatcheur qui part en retraite. On y apporte une simulation faite sur une semaine réelle de tournées, à partir de leur fichier Excel.

## Le client en bref
- 80 camions, environ 120 chauffeurs, logistique (su)
- Tournées planifiées sur Excel par deux dispatcheurs. L'un part en retraite en mars 2027 (su)
- Pénalités de retard cet été chez un gros client de la grande distribution (su). Montant et fréquence `[à vérifier]`
- Il y a 3 semaines, Mme Delvaux a téléchargé notre livre blanc sur les coûts de carburant (su). Le carburant la préoccupe (supposé)
- TMS belge ancien, nom inconnu (su). Interfaces possibles : API, export de fichiers ou rien du tout `[à vérifier]`
- La décision de l'achat revient à Mme Delvaux seule, ou à la direction générale ou au conseil de famille (supposé, à clarifier)

## Nos hypothèses de besoin
1. **Ne pas perdre le savoir du dispatcheur qui part.** Sa connaissance des clients, des créneaux et des contraintes est dans sa tête et dans l'Excel. En mars, un seul dispatcheur ne suffira pas, ou devra former un remplaçant dans l'urgence.
2. **Tenir les délais chez le client de la grande distribution.** Sans visibilité sur les créneaux ni replanification rapide, les pénalités recommenceront et le contrat peut être menacé.
3. **Réduire les kilomètres à vide et le carburant.** Sur 80 camions, quelques pourcents de kilomètres en moins représentent un montant réel. Ce montant est à calculer avec leurs chiffres, pas avec les nôtres.

## Questions de découverte
1. Comment se construit une journée de planification aujourd'hui, de la réception des commandes à la feuille de route du chauffeur ? Combien de temps ça prend ?
2. Que sait faire votre dispatcheur qui part en mars, que personne d'autre ne sait faire ? Qu'est-ce qui est prévu pour son remplacement ?
3. Les retards de cet été : d'où venaient-ils ? Mauvaise planification, imprévus mal gérés, créneaux de quai ?
4. Que vous ont coûté ces pénalités ? Qu'est-ce qui est en jeu avec ce client si ça recommence ?
4. *(pour l'IT)* Quel TMS utilisez-vous ? Comment en sortent les données aujourd'hui : export, base de données accessible, API ? Qui en assure la maintenance ?
6. Quelle part de vos kilomètres est roulée à vide ? Est-ce que vous la mesurez ?
7. Si vous changez d'outil, qui d'autre que vous deux doit donner son accord ? Avec quel budget et quel calendrier ?
8. Pour être prêts en mars, à quelle date faudrait-il que l'outil tourne ?

## Objections probables
| Objection | Piste de réponse | Question de clarification |
|---|---|---|
| « 32 000 € la première année, c'est cher » (80 × 25 € × 12 = 24 000 € + 8 000 € d'intégration) | Comparer avec leurs propres coûts : pénalités, carburant, coût d'un dispatcheur. Ne pas avancer de retour sur investissement sans leurs chiffres | « À quoi vous comparez ce montant ? Combien ont coûté les pénalités de cet été ? » |
| *(IT)* « Notre TMS ne s'interface avec rien » | Toutes les options sont ouvertes (API, échange de fichiers, import manuel au démarrage). On s'engage après avoir vu le TMS, pas avant | « Pouvez-vous nous montrer un export type pendant l'atelier ? » |
| « Nos dispatcheurs connaissent le terrain mieux qu'un logiciel » | Exact. L'outil garde leurs règles et leur laisse le dernier mot. C'est justement ce qui permet de conserver le savoir de celui qui part | « Quelles règles appliquent-ils qu'un outil risque d'ignorer ? » |

## Preuves à mobiliser
- **Frigolux (Liège, 60 camions) : −11 % de kilomètres à vide la première année.** Le chiffre est validé et citable. C'est un transporteur régional de taille voisine. Préciser les différences (activité frigorifique, flotte plus petite) : on ne promet pas les 11 % à Delvaux.
- Si possible, proposer d'organiser un appel avec Frigolux `[à vérifier auprès de Frigolux avant de le proposer]`.

## Conclusion du rendez-vous
> « Vous avez une échéance en mars et un client de la grande distribution à rassurer. Je propose un atelier de 2h avant le 16 octobre, avec [responsable IT] et [dispatcheur partant]. Envoyez-nous d'ici là une semaine type de votre Excel et un export du TMS. On vous montrera ces mêmes tournées recalculées, avec les kilomètres et les créneaux, et on saura si l'intégration est faisable. Mardi ou jeudi, qu'est-ce qui vous arrange ? »

Obtenir une date ferme avant de partir, pas un « on vous recontacte ».

## Après le rendez-vous (sous 24 h)
- Un e-mail récapitulatif : leurs enjeux, dans leurs propres mots, et les chiffres qu'ils ont donnés
- Date et participants de l'atelier, et liste des données à envoyer (semaine type sur Excel, export TMS, contraintes du client de la grande distribution)
- La fiche du cas Frigolux
- Une première estimation du budget (abonnement + intégration), en précisant que le coût d'intégration dépend du TMS

---
**Calendrier :** nous sommes le 28 septembre et le départ est en mars. Si on compte intégration et formation, un démarrage en janvier est déjà serré. Cette urgence est réelle et vient d'eux : c'est votre meilleur argument, à utiliser sans forcer.
