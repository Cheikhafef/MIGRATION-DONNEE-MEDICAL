# 🧠 Migration de données CSV vers MongoDB

Ce projet contient un script Python permettant de **migrer des données depuis un fichier CSV vers une base MongoDB locale**.  
Il est conçu pour faciliter l'importation rapide de données tabulaires dans une base NoSQL, en vue d’analyse, de tests ou de prototypage.

---

## 🎯 Objectif de la migration

L'objectif est de transférer des données structurées (CSV) vers MongoDB en respectant les étapes suivantes :

1. **Lecture du fichier CSV** avec `pandas` pour bénéficier de sa robustesse en traitement de données.  
2. **Transformation des lignes du CSV** en dictionnaires Python, format compatible avec MongoDB.  
3. **Insertion en masse** dans une collection MongoDB via `insert_many`.

Ce processus permet de migrer efficacement des données sans passer par des outils tiers ou des interfaces graphiques.

---

## ⚙️ Prérequis

- **Python 3.13**
- **MongoDB** installé et en cours d'exécution sur `localhost:27017`
- Bibliothèques Python requises :
  ```bash
  pip install pandas pymongo

---

##  🧩 Fonctionnement du script
Le script de migration est disponible dans le fichier `migrationscript.py`.  
Il réalise automatiquement les étapes suivantes :
1. Connexion à MongoDB
2. Lecture du fichier CSV avec `pandas`
3. Transformation des lignes en dictionnaires Python
4. Insertion en masse dans la collection MongoDB via `insert_many`

---

##  📄 Structure des données
{
  "_id": ObjectId("68fe19539b3006c9e4a1f9e8"),
  "Name": "Bobby Jackson",
  "Age": 30,
  "Gender": "Male",
  "Blood Type": "B-",
  "Medical Condition": "Cancer",
  "Date of Admission": "2024-01-31",
  "Doctor": "Matthew Smith",
  "Hospital": "Sons and Miller",
  "Insurance Provider": "Blue Cross",
  "Billing Amount": 18856.28,
  "Room Number": 328,
  "Admission Type": "Urgent",
  "Discharge Date": "2024-02-02",
  "Medication": "Paracetamol",
  "Test Results": "Normal"
}


----

##  📚 Collections MongoDB

📁 Collection : patients

Contient l’ensemble des 5 500 documents importés depuis le fichier CSV.
Une collection joue un rôle similaire à une table dans une base de données relationnelle.

🗃️ Base de données : medical_data

La collection patients est stockée dans une base MongoDB appelée medical_data.
Cette base peut contenir plusieurs collections liées à des informations médicales ou clients.
