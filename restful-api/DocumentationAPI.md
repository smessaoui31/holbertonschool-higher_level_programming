# 1. Consommer des données d’une API avec curl

## 🎯 Objectif

À la fin de cet exercice, vous serez capable de :

- Installer et utiliser `curl` depuis la ligne de commande
- Effectuer des requêtes API simples (GET, POST…)
- Comprendre les réponses API retournées

Encore un grand merci à Hugo Chilemme et Fabien Chavonet pour l'aide apportée à la compréhension des API ! 

Sans oublier mes peers de la C26 , sans qui je pense , je n'aurai pas réussi ce projet.

Place à la documentation maintenant : Je vais essayer de vous montrer ce que j'ai pu apprendre durant toute ma periode de documentation et durant la rédaction de mes lignes de codes ! C'est partit 

---

## 📚 Ressources recommandées

- [Everything curl](https://everything.curl.dev/)
- [Utiliser curl avec des API HTTP](https://reqbin.com/)
- [API publique d'exemple : JSONPlaceholder](https://jsonplaceholder.typicode.com/)

---

## 🧰 Étapes à suivre

### 1️⃣ Installation et vérification

```bash
curl --version
```

Résultat attendu : une version avec les protocoles supportés (http, https…)

### 2️⃣ Requête GET simple

```bash
curl http://example.com
```

Affiche le contenu brut de la page HTML.

### 3️⃣ Récupération de données API JSONPlaceholder

```bash
curl https://jsonplaceholder.typicode.com/posts
```

Vous obtenez un tableau JSON avec plusieurs posts.

### 4️⃣ Affichage uniquement des en-têtes HTTP

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

Réponse typique :

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
...
```

### 5️⃣ Envoi de données avec POST

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Réponse (simulée) :

```json
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```

---

## 💡 Astuces

- `-I` : affiche uniquement les en-têtes (HEAD)
- `-X` : permet de spécifier la méthode HTTP (ex. POST)
- `-d` : permet d’envoyer des données avec la requête
- Pour des réponses JSON plus lisibles : installez `jq`

```bash
curl https://jsonplaceholder.typicode.com/posts | jq .
```

---

## ✅ Résultats attendus

- Vérification de `curl` : version affichée
- Requête GET → Affichage d’une page ou JSON
- Requête HEAD → Affichage des en-têtes uniquement
- Requête POST → Réponse contenant l'objet créé simulé (id: 101)