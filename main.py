import os
print(" Lancement du pipeline complet : Migration  Intégrité  CRUD")
#Lancement du pipeline complet : Migration  Intégrité  CRUD
os.system("python C:\\Users\\cheik\\Desktop\\migration_donnee_medical\\migrationscript.py")
#5500 documents insérés dans MongoDB.
#0
os.system("python C:\\Users\\cheik\\Desktop\\migration_donnee_medical\\test_integrite.py")

#Test d'intégrité entre CSV et MongoDB
#Lignes CSV : 55500 | Lignes MongoDB : 166501
#Colonnes différentes entre CSV et MongoDB.
#Colonnes différentes entre CSV et MongoDB.
#Doublons CSV : 534 | MongoDB : 111534
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
#Types MongoDB :
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
#Room Number           float64
#Admission Type         object
#Discharge Date         object
#Medication             object
#Test Results           object
#Disease                object
#dtype: object
# Test dintégrité terminé.
#0

os.system("python C:\\Users\\cheik\\Desktop\\migration_donnee_medical\\crud_operations.py")

#Démonstration des opérations CRUD :
#Document ajouté :
#{'Age': 45,
#'Disease': 'Flu',
#'Gender': 'Male',
#'Name': 'Jean Dupont',
#'_id': ObjectId('690a656633daa6a47e4c4a7d')}


#Lecture du patient Jean Dupont :
#[{'Age': 45, 'Disease': 'Flu', 'Gender': 'Male', 'Name': 'Jean Dupont'},
#{'Age': 45, 'Disease': 'Flu', 'Gender': 'Male', 'Name': 'Jean Dupont'}]

#Patient mis à jour :
#[{'Age': 46, 'Disease': 'Flu', 'Gender': 'Male', 'Name': 'Jean Dupont'},
#{'Age': 45, 'Disease': 'Flu', 'Gender': 'Male', 'Name': 'Jean Dupont'}]

#Patient supprimé. Vérification :
#[{'Age': 45,
 #'Disease': 'Flu',
 #'Gender': 'Male',
 #'Name': 'Jean Dupont',
 #'_id': ObjectId('690a656633daa6a47e4c4a7d')}]

#CRUD terminé avec succès.
#0