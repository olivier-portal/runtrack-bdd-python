import mysql.connector

import os

import random
from faker import Faker

# Import confidential values from .env
from dotenv import load_dotenv
load_dotenv()

# Get path of .env file
from pathlib import Path
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Get variables from .env
USER = os.getenv("USER")
PASS = os.getenv("PASS")

'''
CREATE DATABASE zoo;
USE zoo;
=> from MySQL
'''

# Connect to server
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=USER,
    password=PASS,
    database="zoo"
    )

# Get a cursor
cur = db.cursor()
class Zoo:
    def __init__(self):
        
        self.create_cage()
        self.create_animal()
        
        # Check that cage table exists
        cage_query = "SELECT superficie, capacite FROM cage"
        cur.execute("SHOW TABLES LIKE 'cage'")
        if cur.fetchone():  # Vérifie si la table existe
            cur.execute(cage_query)
            self.cage = cur.fetchall()
        else:
            self.cage = []

        # Check that table animal exists
        animal_query = "SELECT nom, race, id_cage, naissance, origine FROM animal"
        cur.execute("SHOW TABLES LIKE 'animal'")
        if cur.fetchone():  # Vérifie si la table existe
            cur.execute(animal_query)
            self.animal = cur.fetchall()
        else:
            self.animal = []
        
    # Create table cage
    def create_cage(self):
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cage (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                superficie INT NOT NULL, 
                capacite INT NOT NULL
            )
        """)
        db.commit()
        print("Table 'cage' was successfully created!")
        
    # Create table animal
    def create_animal(self):
        cur.execute("CREATE TABLE IF NOT EXISTS animal (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nom VARCHAR(50) NOT NULL, race VARCHAR(50) NOT NULL, id_cage INT NULL, naissance DATE NOT NULL, origine VARCHAR(50) NOT NULL, FOREIGN KEY (id_cage) REFERENCES cage(id) ON DELETE SET NULL)")
        db.commit()
        print("Table 'animal' created with success !")
        
    # Add cages
    def set_cages(self):    
        cur.execute('''
                INSERT INTO cage (superficie, capacite) VALUES
                    (100, 5),
                    (150, 6),
                    (200, 10),
                    (300, 12),
                    (250, 8),
                    (180, 7),
                    (220, 9),
                    (400, 15),
                    (350, 13),
                    (275, 11)
                ''')        
        db.commit()
        print("cages successfully created !")

#     def add_employe(self):
#         fake = Faker()

#         # Génération de 20 employés
#         employees = []
#         for _ in range(20):
#             nom = fake.last_name()  # Génère un nom de famille
#             prenom = fake.first_name()  # Génère un prénom
#             salaire = round(random.uniform(2000, 8000), 2)  # Salaire aléatoire entre 2k et 8k €
#             id_service = random.randint(1, 5)  # Assumant qu'il y a 5 services
#             employees.append((nom, prenom, salaire, id_service))

#         # Requête SQL pour insérer plusieurs employés
#         query_employe = """
#         INSERT INTO employe (nom, prenom, salaire, id_service) 
#         VALUES (%s, %s, %s, %s);
#         """

#         # Exécuter l'insertion
#         cur.executemany(query_employe, employees)
#         db.commit()
#         print("20 employés ajoutés avec succès !")
        
#     def get_employes_services(self):
#         query = """
#         SELECT employe.nom, employe.prenom, service.nom AS service
#         FROM employe
#         JOIN service ON employe.id_service = service.id
#         """
        
#         cur.execute(query)
#         results = cur.fetchall()
        
#         for row in results:
#             print(f"{row[1]} { row[0]} travaille au service {row[2]}")
            
#     def get_employe_name(self):
#         for employe in self.employes:
#             print(f"{employe[1]} {employe[0]}")
            
#     def get_employe_income(self):
#         for employe in self.employes:
#             print(f"Le salaire de {employe[1]} {employe[0]} est de: {employe[2]}")
            
#     def get_sum_incomes(self):
#         cur.execute("SELECT SUM(salaire) FROM employe")
#         result = cur.fetchone()[0]
#         print(f"La masse salariale coûte {result}€ par mois à La Plateforme")
        
#     def get_average_income(self):
#         cur.execute("SELECT AVG(salaire) FROM employe")
#         result = cur.fetchone()[0]
#         print(f"Le salaire médian à La Plateforme est de: {result}€ par mois")
        
#     def update_income(self):
#         update_income_query = '''
#             UPDATE employe
#             SET salaire = 2675.21
#             WHERE nom = "Smith" AND prenom = "Lee"
#             '''
#         cur.execute(update_income_query)
#         db.commit()

#         employe_query = '''
#             SELECT nom, prenom, salaire FROM employe
#             WHERE nom = "Smith" AND prenom = "Lee"
#         '''
#         cur.execute(employe_query)
#         updated_employe = cur.fetchone()
#         print(f"Le salaire de {updated_employe[1]} {updated_employe[0]} est désormais de {updated_employe[2]}€")
        
#     def delete_employe(self):
#         employe_query = '''
#             SELECT nom, prenom FROM employe
#             WHERE nom = "Hill" AND prenom = "Tammie"
#         '''
#         cur.execute(employe_query)
#         employe = cur.fetchone()
        
#         if employe:
#             del_employe_query = '''
#                 DELETE FROM employe
#                 WHERE nom = "Hill" AND prenom = "Tammie"
#             '''
#             cur.execute(del_employe_query)
#             db.commit()
            
#             print(f"Le salarié {employe[1]} {employe[0]} a malheureusement quitté l'entreprise.")
#         else:
#             print("Aucun employé trouvé avec ce nom et prénom.")

# Create an instance of Employe Class
employe_instance = Zoo()

# # call methods from the instance
# '''
employe_instance.create_cage()
# employe_instance.set_cages()
employe_instance.create_animal()
# employe_instance.add_employe()

# Used only once
# '''
# employe_instance.get_employe_name()
# employe_instance.get_employes_services()
# employe_instance.get_employe_income()
# employe_instance.get_sum_incomes()
# employe_instance.get_average_income()
# employe_instance.update_income()
# employe_instance.delete_employe()

cur.close()
db.close()