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

# Connect to server
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=USER,
    password=PASS,
    database="laplateforme"
    )

# Get a cursor
cur = db.cursor()
class Employe:
    def __init__(self):
        cur.execute("SELECT nom, prenom, salaire, id_service FROM employe")
        self.employes = cur.fetchall()
        
    # Create table service
    def create_service(self):
        cur.execute("CREATE TABLE IF NOT EXISTS service (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50) NOT NULL)")
        db.commit()
        print("Table 'service' créée avec succès !")
        
    # Add services
    def insert_services(self):
        services = [("Informatique",), ("RH",), ("Comptabilité",), ("Marketing",), ("Direction",)]
        
        query_service = "INSERT INTO service (nom) VALUES (%s);"
        cur.executemany(query_service, services)
        
        db.commit()
        print("Services ajoutés avec succès !")
        
    # Create table employe
    def create_employe(self):
        cur.execute("CREATE TABLE IF NOT EXISTS employe (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nom VARCHAR(100) NOT NULL, prenom VARCHAR(100) NOT NULL, salaire FLOAT(8, 2) NOT NULL, id_service INT NOT NULL, FOREIGN KEY (id_service) REFERENCES service(id) ON DELETE CASCADE)")
        db.commit()
        print("Table 'employe' créée avec succès !")

    def add_employe(self):
        fake = Faker()

        # Génération de 20 employés
        employees = []
        for _ in range(20):
            nom = fake.last_name()  # Génère un nom de famille
            prenom = fake.first_name()  # Génère un prénom
            salaire = round(random.uniform(2000, 8000), 2)  # Salaire aléatoire entre 2k et 8k €
            id_service = random.randint(1, 5)  # Assumant qu'il y a 5 services
            employees.append((nom, prenom, salaire, id_service))

        # Requête SQL pour insérer plusieurs employés
        query_employe = """
        INSERT INTO employe (nom, prenom, salaire, id_service) 
        VALUES (%s, %s, %s, %s);
        """

        # Exécuter l'insertion
        cur.executemany(query_employe, employees)
        db.commit()
        print("20 employés ajoutés avec succès !")
        
    def get_employes_services(self):
        query = """
        SELECT employe.nom, employe.prenom, service.nom AS service
        FROM employe
        JOIN service ON employe.id_service = service.id
        """
        
        cur.execute(query)
        results = cur.fetchall()
        
        for row in results:
            print(f"{row[1]} { row[0]} travaille au service {row[2]}")
            
    def get_employe_name(self):
        for employe in self.employes:
            print(f"{employe[1]} {employe[0]}")
            
    def get_employe_income(self):
        for employe in self.employes:
            print(f"Le salaire de {employe[1]} {employe[0]} est de: {employe[2]}")
            
    def get_sum_incomes(self):
        cur.execute("SELECT SUM(salaire) FROM employe")
        result = cur.fetchone()[0]
        print(f"La masse salariale coûte {result}€ par mois à La Plateforme")
        
    def get_average_income(self):
        cur.execute("SELECT AVG(salaire) FROM employe")
        result = cur.fetchone()[0]
        print(f"Le salaire médian à La Plateforme est de: {result}€ par mois")
        
    def update_income(self):
        update_income_query = '''
            UPDATE employe
            SET salaire = 2675.21
            WHERE nom = "Smith" AND prenom = "Lee"
            '''
        cur.execute(update_income_query)
        db.commit()

        employe_query = '''
            SELECT nom, prenom, salaire FROM employe
            WHERE nom = "Smith" AND prenom = "Lee"
        '''
        cur.execute(employe_query)
        updated_employe = cur.fetchone()
        print(f"Le salaire de {updated_employe[1]} {updated_employe[0]} est désormais de {updated_employe[2]}€")
        
    def delete_employe(self):
        employe_query = '''
            SELECT nom, prenom FROM employe
            WHERE nom = "Hill" AND prenom = "Tammie"
        '''
        cur.execute(employe_query)
        employe = cur.fetchone()
        
        if employe:
            del_employe_query = '''
                DELETE FROM employe
                WHERE nom = "Hill" AND prenom = "Tammie"
            '''
            cur.execute(del_employe_query)
            db.commit()
            
            print(f"Le salarié {employe[1]} {employe[0]} a malheureusement quitté l'entreprise.")
        else:
            print("Aucun employé trouvé avec ce nom et prénom.")

# Create an instance of Employe Class
employe_instance = Employe()

# call methods from the instance
'''
employe_instance.create_service()
employe_instance.insert_services()
employe_instance.create_employe()
employe_instance.add_employe()

Used only once
'''
employe_instance.get_employe_name()
employe_instance.get_employes_services()
employe_instance.get_employe_income()
employe_instance.get_sum_incomes()
employe_instance.get_average_income()
employe_instance.update_income()
employe_instance.delete_employe()

cur.close()
db.close()