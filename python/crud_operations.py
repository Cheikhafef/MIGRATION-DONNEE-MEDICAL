from pymongo import MongoClient
from pprint import pprint
## Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["medical_data"]
collection = db["patients"]
print("\n Démonstration des opérations CRUD :")
#Démonstration des opérations CRUD :

# CREATE
nouveau_patient = {"Name": "Jean Dupont", "Age": 45, "Gender": "Male", "Disease": "Flu"}
collection.insert_one(nouveau_patient)
#InsertOneResult(ObjectId('690a3501607d7f5226eeb79b'), acknowledged=True)

print(" Document ajouté :")
#Document ajouté :
pprint(nouveau_patient)
#{'Age': 45,
#'Disease': 'Flu',
# 'Gender': 'Male',
# 'Name': 'Jean Dupont',
# '_id': ObjectId('690a3501607d7f5226eeb79b')

# READ
print("\n Lecture du patient Jean Dupont :")
#Lecture du patient Jean Dupont :
pprint(list(collection.find({"Name": "Jean Dupont"}, {"_id": 0})))
#[{'Age': 45, 'Disease': 'Flu', 'Gender': 'Male', 'Name': 'Jean Dupont'}]

# UPDATE
collection.update_one({"Name": "Jean Dupont"}, {"$set": {"Age": 46}})
#UpdateResult({'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)

print("\n Patient mis à jour :")
#Patient mis à jour :
pprint(list(collection.find({"Name": "Jean Dupont"}, {"_id": 0})))
#[{'Age': 46, 'Disease': 'Flu', 'Gender': 'Male', 'Name': 'Jean Dupont'}]

# DELETE
collection.delete_one({"Name": "Jean Dupont"})
#DeleteResult({'n': 1, 'ok': 1.0}, acknowledged=True)

print("\n Patient supprimé. Vérification :")

#Patient supprimé. Vérification :
pprint(list(collection.find({"Name": "Jean Dupont"})))
#[]

print("\n CRUD terminé avec succès.")
#CRUD terminé avec succès.