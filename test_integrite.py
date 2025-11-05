import pandas as  pd
from pymongo import MongoClient
# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["medical_data"]
collection = db["patients"]
# Charger le CSV original
df_csv = pd.read_csv("C:/Users/cheik/Desktop/migration_donnee_medical/healthcare_dataset.csv")
# Charger les données depuis MongoDB
mongo_docs = list(collection.find({}, {"_id": 0}))
df_mongo = pd.DataFrame(mongo_docs)
# --- TESTS D'INTÉGRITÉ ---
print("\n Test d'intégrité entre CSV et MongoDB")

#Test d'intégrité entre CSV et MongoDB
# 1️⃣ Nombre de lignes
print(f"Lignes CSV : {len(df_csv)} | Lignes MongoDB : {len(df_mongo)}")
#lignes CSV : 55500 | Lignes MongoDB : 55500

if len(df_csv) == len(df_mongo):
    print(" Nombre de lignes identique.")
else:
    print(" Colonnes différentes entre CSV et MongoDB.")

#Nombre de lignes identique.

# 2️⃣ Colonnes
if list(df_csv.columns) == list(df_mongo.columns):
    print(" Colonnes identiques.")
else:
    print(" Colonnes différentes entre CSV et MongoDB.")
...
#Colonnes identiques.
# 3️⃣ Doublons / Valeurs manquantes
print(f"Doublons CSV : {df_csv.duplicated().sum()} | MongoDB : {df_mongo.duplicated().sum()}")
#Doublons CSV : 534 | MongoDB : 534

# 4️⃣ Vérification de la structure (types)
#types CSV :
print(df_csv.dtypes)
#Name                   object
#Age                     int64
#Gender                 object
#Blood Type             object
#Medical Condition      object
#Date of Admission      object
#Doctor                 object
#Hospital               object
#Insurance Provider     object
#Billing Amount        float64
#Room Number             int64
#Admission Type         object
#Discharge Date         object
#Medication             object
#Test Results           object
#dtype: object

print("\nTypes MongoDB :")

#Types MongoDB :
print(df_mongo.dtypes)
#Name                   object
#Age                     int64
#Gender                 object
#Blood Type             object
#Medical Condition      object
#Date of Admission      object
#Doctor                 object
#Hospital               object
#Insurance Provider     object
#Billing Amount        float64
#Room Number             int64
#Admission Type         object
#Discharge Date         object
#Medication             object
#Test Results           object
#dtype: object

print("\n Test dintégrité terminé.")

#Test dintégrité terminé