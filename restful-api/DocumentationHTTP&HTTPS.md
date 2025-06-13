# 0. Basics of HTTP/HTTPS

## 🌐 Objectif

L'objectif de ce README vient de l'idée de l'école Holberton afin que nous documentions nos projets sur les RESTFULL API et comment ces dernières fonctionnent.

Les buts de ces projets sont diverses et variés et les voici :

- Faire la différence entre HTTP et HTTPS
- Comprendre la structure de base d'une requête/réponse HTTP
- Reconnaître et expliquer les méthodes HTTP et les codes de statut les plus courants.

A noter que les ressources ainsi que la documentation sont très riches concernant ce sujet et que les vidéos explicatives sur Youtube par exemple sont très enrichissantes.

Pour ma part je vous en recommande trois qui m'ont beaucoup aidé à la documentation ainsi qu'à l'enrichissement dans le domaine des API.

Je tiens à remercier mes mates de la cohorte C26 de l'école Holberton pour l'aide qu'ils m'ont apporté notamment à la task 05 de ce projet.

---

## 📖 Ressources recommandées

- [MDN - Vue d'ensemble du protocole HTTP](https://developer.mozilla.org/fr/docs/Web/HTTP/Overview)
- [Différence entre HTTP et HTTPS](https://www.ssl.com/faqs/what-is-the-difference-between-http-and-https/)
- [Liste des codes de statut HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## 🔐 Différences entre HTTP et HTTPS

| Critère             | HTTP                        | HTTPS                                 |
|---------------------|-----------------------------|----------------------------------------|
| Sécurité            | Aucune                      | Données chiffrées via SSL/TLS         |
| Port par défaut     | 80                          | 443                                    |
| Préfixe de l’URL    | `http://`                   | `https://`                             |
| Utilisation typique | Sites simples, test locaux  | Sites sensibles : paiements, emails   |

> Le `s` dans HTTPS signifie "secure".

---

## 📦 Structure d’une requête et réponse HTTP

### 📨 Requête HTTP (exemple d’un GET) :

```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### 📬 Réponse HTTP :

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html>
  ...
</html>
```

---

## 🔧 Méthodes HTTP courantes

| Méthode | Description                             | Cas d’utilisation                            |
|---------|-----------------------------------------|----------------------------------------------|
| GET     | Récupérer des données                   | Accéder à une page Web ou API                |
| POST    | Envoyer des données                     | Envoyer un formulaire                        |
| PUT     | Modifier/Remplacer des données existantes| Mise à jour complète d’un enregistrement     |
| DELETE  | Supprimer des données                   | Suppression d’un utilisateur dans une API    |

---

## 📊 Codes de statut HTTP courants

| Code | Signification            | Scénario typique                                    |
|------|--------------------------|-----------------------------------------------------|
| 200  | OK                       | Requête réussie                                     |
| 301  | Moved Permanently        | Redirection permanente d’un site                    |
| 400  | Bad Request              | Données manquantes ou mal formées                   |
| 404  | Not Found                | Ressource non trouvée sur le serveur                |
| 500  | Internal Server Error    | Erreur interne du serveur                          |

---

## 🧪 Astuces

- Utilisez l'outil développeur (F12 → Réseau) pour analyser les requêtes/réponses.
- Utilisez Wireshark (facultatif) pour voir la différence entre trafic HTTP et HTTPS.