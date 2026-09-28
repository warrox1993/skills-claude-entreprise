# Revue de la politique de mots de passe (version 2017)

## Synthèse

Votre plus gros risque n'est pas dans le texte de la politique. Il vient de deux choses : aucun compte n'a de MFA à part celui du gérant, et le compte « admin@ » est partagé entre trois personnes, dont un prestataire externe. Un seul mot de passe hameçonné ou noté sur un post-it peut donner accès à toute la messagerie, au VPN, à la gestion de portefeuille et aux données de vos assurés.

Les trois changements les plus importants :

1. **MFA pour tout le monde** sur Microsoft 365, le VPN et le logiciel de gestion. Les comptes administrateurs passent en premier.
2. **Supprimer le compte « admin@ » partagé.** Chaque administrateur reçoit un compte à son nom, séparé de son compte de tous les jours.
3. **Arrêter le changement tous les 60 jours et l'obligation de mélanger majuscules, chiffres et symboles.** On les remplace par une phrase de passe longue, un contrôle contre les mots de passe compromis et un gestionnaire de mots de passe fourni par la société. C'est ce qui fera disparaître les post-it.

Il faut aussi corriger en urgence la règle 6 (« sauf au service IT si celui-ci le demande »). C'est exactement la phrase qu'un escroc au faux support informatique espère lire.

## Analyse règle par règle

| Règle actuelle | Verdict | Pourquoi | Proposition |
|---|---|---|---|
| 1. 8 caractères minimum avec majuscule, minuscule, chiffre et caractère spécial | **Modifier** | La composition imposée produit des mots de passe prévisibles (« Printemps2026! ») sans vraie sécurité en plus. NIST SP 800-63B rév. 4 recommande de ne plus l'imposer et de miser sur la longueur : au moins 15 caractères si le mot de passe est le seul facteur, au moins 8 s'il est combiné à la MFA. | Au moins 12 caractères, sans obligation de composition, phrases de passe et espaces acceptés. Au moins 15 caractères pour les comptes administrateurs. |
| 2. Changement tous les 60 jours, 12 derniers mots de passe interdits | **Supprimer** | Les changements forcés poussent aux variantes (« …01 », « …02 ») et aux post-it, comme vos commerciaux le montrent. NIST déconseille le changement périodique. | Changement seulement en cas de suspicion de compromission, de fuite détectée ou de départ d'un administrateur. |
| 3. Blocage après 3 tentatives, déblocage par l'IT | **Modifier** | Trois essais, c'est très bas. Cela génère des appels au support, et un attaquant peut bloquer volontairement des comptes. Entra ID dispose d'un verrouillage intelligent qui limite les tentatives sans pénaliser l'utilisateur légitime. | Limitation automatique des tentatives (verrouillage intelligent Entra ID), déblocage par l'utilisateur via la réinitialisation en libre-service avec MFA. |
| 4. Pas de prénom ni de nom | **Garder et élargir** | L'idée est bonne mais trop étroite. | Refus des mots de passe connus ou compromis, ainsi que ceux qui contiennent le nom de la société, du produit, etc. Techniquement, c'est la liste d'interdiction d'Entra ID Password Protection. |
| 5. Question secrète pour la réinitialisation | **Supprimer** | Les réponses se trouvent souvent sur les réseaux sociaux ou se devinent. NIST et l'ANSSI les déconseillent. | Réinitialisation en libre-service validée par la MFA. Par le support, uniquement après vérification d'identité (voir la politique révisée). |
| 6. Interdit de communiquer son mot de passe, sauf au service IT s'il le demande | **Modifier (urgent)** | L'exception légitime l'arnaque au faux support, l'une des attaques les plus courantes. Un administrateur n'a jamais besoin du mot de passe d'un utilisateur. | Ne jamais communiquer son mot de passe ni un code MFA, à personne, y compris l'IT, le gérant ou le prestataire. Toute demande de ce type est signalée. |
| 7. Même mot de passe autorisé pour la messagerie et le logiciel de gestion | **Supprimer** | Si l'un des deux fuit, l'autre tombe aussi. | Soit le logiciel de gestion accepte la connexion via Microsoft (SSO Entra ID), et il n'y a plus qu'un seul compte, protégé par la MFA. Soit il faut un mot de passe différent, stocké dans le gestionnaire de mots de passe. |

## Règles manquantes

| Règle à ajouter | Pourquoi | Priorité |
|---|---|---|
| MFA obligatoire pour tous les utilisateurs sur Microsoft 365, le VPN et le logiciel de gestion | C'est la mesure qui bloque la grande majorité des prises de contrôle de comptes par hameçonnage ou réutilisation de mots de passe. Votre assureur cyber l'exige probablement déjà. | **Critique** |
| Comptes administrateurs nominatifs et séparés, plus de compte « admin@ » partagé | Aujourd'hui, impossible de savoir qui a fait quoi. Le prestataire ne peut pas être révoqué sans changer le mot de passe des deux autres. Si ce compte n'a pas de MFA, c'est la clé de toute la société. | **Critique** |
| MFA résistante à l'hameçonnage pour les administrateurs (clé FIDO2 ou passkey) | Les kits d'hameçonnage actuels contournent les codes et les notifications push. | Haute |
| Blocage des protocoles d'authentification anciens (POP, IMAP, SMTP authentifié, anciens clients Office) | Ils contournent la MFA. | Haute |
| Deux comptes d'urgence (« bris de glace ») | Ils évitent de perdre l'accès au tenant si la MFA ou l'accès conditionnel est mal configuré. Ils sont surveillés et leurs identifiants sont conservés sous scellé. | Haute |
| Gestionnaire de mots de passe fourni par la société | Il donne un mot de passe unique par service sans effort de mémoire, et remplace les post-it. | Haute |
| Procédure de vérification d'identité pour les réinitialisations par le support | Les appels « j'ai perdu mon téléphone, réinitialise ma MFA » sont une cible classique. | Haute |
| Accès et départ du prestataire externe | Compte nominatif, droits limités à ce qui est nécessaire, révocation à la fin du contrat. | Moyenne |
| Procédure de départ d'un collaborateur | Désactivation des comptes le jour même, révocation des sessions et des appareils MFA. | Moyenne |
| Déverrouillage du poste par Windows Hello (code PIN ou biométrie) | Moins de mots de passe à taper au quotidien, meilleure acceptation. | Basse |

## Politique révisée

> **Politique d'authentification, [Nom de la société]**
> Version 2.0, [date], validée par : [gérant]
>
> **Pourquoi cette politique**
> Nous traitons des données personnelles et financières de nos clients. Un seul compte piraté peut exposer ces données et permettre des fraudes, par exemple de faux ordres de virement. Cette politique est volontairement courte : merci de l'appliquer entièrement.
>
> **1. Vérification en deux étapes (MFA)**
> La connexion à la messagerie et à Microsoft 365, au VPN et au logiciel de gestion de portefeuille exige une vérification en deux étapes via l'application d'authentification installée sur votre téléphone professionnel ou personnel. Si vous recevez une demande de validation que vous n'avez pas déclenchée, refusez-la et prévenez immédiatement [responsable IT].
>
> **2. Choisir son mot de passe**
> - Au moins 12 caractères. Nous recommandons une phrase de passe de plusieurs mots, par exemple quatre mots sans lien entre eux. Les espaces sont autorisés.
> - Aucune obligation de mettre des majuscules, chiffres ou symboles.
> - Les mots de passe trop courants ou déjà apparus dans des fuites de données sont refusés automatiquement.
> - N'utilisez pas votre nom, le nom de la société ou un mot de passe que vous utilisez ailleurs, surtout pour un usage personnel.
>
> **3. Un mot de passe différent par service**
> Chaque service a son propre mot de passe. La société met à votre disposition un gestionnaire de mots de passe : c'est le seul endroit où les noter. Les post-it, carnets et fichiers Excel de mots de passe sont interdits.
>
> **4. Changement du mot de passe**
> Vous n'avez plus à changer votre mot de passe à date fixe. Vous devez le changer immédiatement si vous pensez qu'il a été vu, saisi sur un faux site ou divulgué, ou si l'IT vous le demande à la suite d'un incident.
>
> **5. Ne jamais communiquer son mot de passe**
> Ne communiquez jamais votre mot de passe ni un code de vérification, à personne : ni un collègue, ni le gérant, ni le service IT, ni le prestataire informatique. Personne n'en a besoin pour travailler. Toute demande de ce type, par téléphone, e-mail ou Teams, est une tentative d'escroquerie : signalez-la à [responsable IT].
>
> **6. Mot de passe oublié ou compte bloqué**
> Utilisez la réinitialisation en libre-service ([lien]), qui vous demande votre vérification en deux étapes. Si c'est impossible (téléphone perdu, par exemple), contactez [responsable IT]. Votre identité sera vérifiée, en personne ou par un rappel sur votre numéro enregistré, avant toute réinitialisation.
>
> **7. Comptes administrateurs**
> - Chaque administrateur dispose d'un compte d'administration à son nom, distinct de son compte habituel, utilisé uniquement pour les tâches d'administration.
> - Les comptes d'administration partagés sont interdits.
> - Les comptes d'administration utilisent une vérification résistante à l'hameçonnage (clé de sécurité ou passkey) et un mot de passe d'au moins 15 caractères.
> - Le prestataire externe dispose de son propre compte, limité aux droits nécessaires, désactivé à la fin du contrat.
> - Deux comptes d'urgence existent. Leurs identifiants sont conservés sous scellé et toute utilisation est contrôlée.
>
> **8. Arrivées et départs**
> Les comptes d'un collaborateur ou d'un prestataire qui quitte la société sont désactivés le jour de son départ.
>
> **9. Signaler un incident**
> Clic sur un lien suspect, mot de passe saisi sur un site douteux, appareil perdu : prévenez immédiatement [responsable IT, téléphone]. Un signalement rapide n'est jamais reproché.

## Plan de mise en œuvre

| Étape | Contenu | Public | Durée estimée | Prérequis |
|---|---|---|---|---|
| 1. Sécuriser l'administration (semaine 1) | Créer trois comptes admin nominatifs (gérant, responsable IT, prestataire) avec les seuls rôles nécessaires. Créer deux comptes bris de glace. MFA sur tous ces comptes. Retirer les droits admin de « admin@ » puis le désactiver. Changer tous les mots de passe connus de ce compte (VPN, logiciel de gestion, etc.). | 3 admins | 1 à 2 jours | Inventaire de là où « admin@ » est utilisé (connecteurs, licences, boîtes partagées) |
| 2. Corriger la règle 6 tout de suite | Envoyer un message à tous : « l'IT ne vous demandera jamais votre mot de passe ». | Tous | 1 heure | Aucun |
| 3. Préparer la MFA | Choisir entre les paramètres de sécurité par défaut (gratuits) et l'accès conditionnel (Entra ID P1, inclus dans Microsoft 365 Business Premium). Activer l'inscription combinée MFA et réinitialisation en libre-service. | Responsable IT et prestataire | 2 à 3 jours | Connaître vos licences |
| 4. Déployer la MFA sur Microsoft 365 (semaines 2 et 3) | Session de 20 minutes ou court guide. Inscription assistée par groupes : bureau d'abord, puis commerciaux. Bloquer ensuite l'authentification ancienne. | Tous | 2 semaines | Étape 3, téléphones disponibles (solution de repli pour ceux qui n'ont pas de smartphone : clé FIDO2) |
| 5. MFA sur le VPN et le logiciel de gestion (semaines 3 à 6) | VPN : connexion via Entra ID (SAML) ou extension NPS/RADIUS selon le modèle. Logiciel de gestion : demander à l'éditeur s'il gère le SSO Microsoft, sinon sa propre MFA. | Tous | 2 à 4 semaines | Réponse de l'éditeur et du fournisseur du VPN |
| 6. Nouvelles règles de mot de passe | Désactiver l'expiration à 60 jours. Activer la liste d'interdiction personnalisée (Password Protection). Ajuster le verrouillage intelligent. | Responsable IT | 1 jour | MFA déployée (on assouplit l'expiration une fois la MFA en place) |
| 7. Gestionnaire de mots de passe | Choisir un outil professionnel avec coffres partagés et journalisation, déployer, former, supprimer les post-it. | Tous | 2 à 4 semaines | Budget |
| 8. Diffusion et suivi | Publier la politique 2.0, la faire signer ou l'intégrer au règlement intérieur, faire un point à 3 mois sur les incidents et appels au support. | Tous | Continu | Étapes précédentes |

Pour les commerciaux, présentez le changement comme un gain : plus de changement tous les deux mois, un seul geste de validation sur le téléphone, et un gestionnaire qui retient les mots de passe à leur place.

## Points à vérifier

- **Longueur minimale dans Entra ID** : pour les comptes uniquement cloud, Entra ID impose 8 caractères minimum et ce seuil n'est, à ma connaissance, pas paramétrable. La règle des 12 caractères reposera donc sur la communication et la liste d'interdiction, sauf si vous avez un Active Directory local synchronisé, où la stratégie de domaine s'applique. Vérifiez votre configuration (cloud seul ou hybride).
- **Licences** : l'accès conditionnel et Password Protection pour un AD local demandent Entra ID P1. Vérifiez si vous êtes en Business Basic/Standard ou en Business Premium. Les paramètres de sécurité par défaut et l'accès conditionnel ne peuvent pas être actifs en même temps.
- **Expiration des mots de passe** : réglage dans le centre d'administration Microsoft 365 (Paramètres > Paramètres de l'organisation > Sécurité et confidentialité > Stratégie d'expiration des mots de passe), et dans la GPO de domaine si vous avez un AD local.
- **VPN** : le modèle et la version déterminent la méthode d'intégration MFA (SAML Entra ID, RADIUS avec l'extension NPS, ou la solution MFA propre au fournisseur).
- **Logiciel de gestion de portefeuille** : prise en charge du SSO (SAML ou OpenID Connect) ou d'une MFA native. À demander à l'éditeur.
- **Référentiels** : NIST SP 800-63B rév. 4 (publiée en 2025), guide de l'ANSSI sur l'authentification multifacteur et les mots de passe, recommandations du CCB (Safeonweb@work, CyberFundamentals) si vous êtes en Belgique. Vérifiez leur version en vigueur.
- **Cadre réglementaire** : le RGPD (article 32, sécurité du traitement) s'applique dans tous les cas, surtout si vous traitez des données de santé (assurances vie, santé, invalidité). DORA exclut en principe les intermédiaires d'assurance qui sont des PME, et le courtage n'est normalement pas un secteur NIS2. Faites-le confirmer par votre conseil ou votre fédération professionnelle, et vérifiez aussi les exigences de votre autorité de contrôle et de votre propre assurance cyber, qui impose souvent la MFA.
- **Validation** : avec des données clients sensibles et un prestataire qui a des droits d'administration, faites valider la configuration finale (accès conditionnel, comptes d'urgence, rôles) par le prestataire ou un spécialiste sécurité. Une erreur d'accès conditionnel peut bloquer tout le monde, y compris les administrateurs.
