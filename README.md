# 🧠 Migration de données médicales vers MongoDB (Docker + Python)

## 📘 Contexte du projet

 L'objectif de ce projet est de **migrer un dataset de données médicales** depuis un fichier CSV vers une base de données **MongoDB**,afin d’améliorer la **scalabilité** et la **performance** du système de gestion des données du client.
---
## 🎯 Objectifs

* Automatiser la migration des données d’un fichier CSV vers MongoDB
* Conteneuriser la solution avec **Docker** pour la rendre portable et scalable
* Vérifier l’intégrité des données avant et après migration
* Implémenter les opérations **CRUD (Create, Read, Update, Delete)**
* Étudier les possibilités de déploiement sur **AWS (Amazon Web Services)**
* Versionner et documenter le projet sur **GitHub**
---
## 🧱 Architecture du projet

```
migration-project/
│
├── docker-compose.yml         # Déploie MongoDB et le script Python dans deux conteneurs
├── Dockerfile                 # Image Python avec les dépendances
├── migrationscript.py         # Script principal de migration CSV → MongoDB
├── crud_operations.py         # Script CRUD (Create, Read, Update, Delete)
├── test_integrite.py          # Script de test d’intégrité des données
├── requirements.txt           # Liste des dépendances Python
├── healthcare_dataset.csv     # Dataset médical fourni
├── mongodb.md                 # Documentation technique de la base
└── README.md                  # Documentation du projet (ce fichier)
```

---

## ⚙️ Technologies utilisées

| Technologie                 | Rôle                                               |
| --------------------------- | -------------------------------------------------- |
| **Python 3.13**             | Langage principal (migration + tests)              |
| **Pandas**                  | Manipulation et analyse du fichier CSV             |
| **PyMongo**                 | Connexion et opérations MongoDB                    |
| **MongoDB**                 | Base de données NoSQL utilisée                     |
| **Docker / Docker Compose** | Conteneurisation et orchestration                  |
| **AWS (recherche)**         | Étude pour déploiement cloud (ECS, S3, DocumentDB) |

---

## 🐳 Déploiement avec Docker Compose

### 🔧 1. Construire et lancer les conteneurs

```bash
docker-compose up --build
```

### 📦 2. Conteneurs créés

* `mongodb` : service de base de données MongoDB
* `migration` : exécute automatiquement le script `migrationscript.py`

### 🧠 3. Volumes utilisés

| Volume         | Rôle                            |
| -------------- | ------------------------------- |
| `mongodb_data` | Persistance des données MongoDB |
| `csv_data`     | Stockage des fichiers CSV       |

### 🧠 4. Réseau Docker

Les conteneurs communiquent via le réseau interne `mongo-net`.


### 💾 Configuration avec fichier `.env`

Pour éviter de mettre les identifiants directement dans le fichier `docker-compose.yml`, on peut les définir dans un fichier `.env`.

Crée un fichier nommé `.env` à la racine du projet avec les informations suivantes :

```bash
# Variables MongoDB
MONGO_ADMIN=${MONGO_ADMIN}
MONGO_PASSWORD=${MONGO_PASSWORD}
MONGO_HOST=${MONGO_HOST}
MONGO_PORT=${MONGO_PORT}
MONGO_URI=mongodb://${MONGO_ADMIN}:${MONGO_PASSWORD}@${MONGO_HOST}:${MONGO_PORT}/

```

---
### Tests d’intégrité
Avant et après la migration, le script `test_integrite.py` :

* Compare le nombre de lignes entre le CSV et MongoDB
* Vérifie les colonnes et leurs types
* Détecte les doublons et valeurs manquantes

**Exécution :**

```bash
python test_integrite.py
```

---

##  Opérations CRUD

Le script `crud_operations.py` permet d’effectuer des opérations sur la base :

```python
# CREATE
collection.insert_one({"Name": "Jean Dupont", "Age": 45, "Disease": "Flu"})

# READ
collection.find({"Name": "Jean Dupont"})

# UPDATE
collection.update_one({"Name": "Jean Dupont"}, {"$set": {"Age": 46}})

# DELETE
collection.delete_one({"Name": "Jean Dupont"})
```

##  Authentification MongoDB

Le service MongoDB est protégé par un utilisateur et mot de passe :

| Paramètre        | Valeur         |
| ---------------- | -------------- |
| **Utilisateur**  | `admin`        |
| **Mot de passe** | `admin123`     |
| **Base**         | `medical_data` |

Ces identifiants sont définis dans `docker-compose.yml` :

```yaml
environment:
  MONGO_INITDB_ROOT_USERNAME: admin
  MONGO_INITDB_ROOT_PASSWORD: admin123
  MONGO_INITDB_DATABASE: medical_data
```

---

## 📊 Résultats obtenus

* Migration réussie de **1000+ enregistrements** depuis le CSV
* Données intègres après importation
* Tests CRUD fonctionnels
* Conteneur Docker reproductible sur n’importe quelle machine
* Architecture prête pour un déploiement cloud (AWS)

---

## Auteur

* **Nom :** [CHEIKH afef]
* **Formation :** Big Data / DevOps - France Travail
* **GitHub :** [https://github.com/Cheikhafef/migration-donnee-medicale]

---

##  Commandes utiles

```bash
# Lancer la migration
python migrationscript.py

# Tester l’intégrité
python test_integrite.py

# Tester le CRUD
python crud_operations.py

# Lancer avec Docker Compose
docker-compose up --build
```

