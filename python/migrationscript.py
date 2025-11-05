import pandas as pd
from pymongo import MongoClient

# Connexion à MongoDB local (sans authentification)
client = MongoClient("mongodb://localhost:27017/")

# Création ou sélection de la base de données
db = client["medical_data"]

# Création ou sélection de la collection
collection = db["patients"]

# Charger le fichier CSV (chemin complet vers ton fichier)
df = pd.read_csv("C:/Users/cheik/Desktop/migration_donnee_medical/healthcare_dataset.csv")

# Convertir le DataFrame en liste de dictionnaires (format MongoDB)
records = df.to_dict(orient="records")

# Insérer les documents dans MongoDB
collection.insert_many(records)

print(f"✅ {len(records)} documents insérés dans MongoDB.")