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

# Create table employe
def create_employe():
    cur.execute("CREATE TABLE IF NOT EXISTS employe (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nom VARCHAR(100) NOT NULL, prenom VARCHAR(100) NOT NULL, salaire FLOAT(8, 2) NOT NULL, id_service INT NOT NULL, FOREIGN KEY (id_service) REFERENCES service(id) ON DELETE CASCADE)")
    db.commit()
    print("Table 'employe' créée avec succès !")

def add_employe():
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
    
# Create table service
def create_service():
    cur.execute("CREATE TABLE IF NOT EXISTS service (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50) NOT NULL)")
    db.commit()
    print("Table 'service' créée avec succès !")
    
# Add services
def insert_services():
    services = [("Informatique",), ("RH",), ("Comptabilité",), ("Marketing",), ("Direction",)]
    
    query_service = "INSERT INTO service (nom) VALUES (%s);"
    cur.executemany(query_service, services)
    
    db.commit()
    print("Services ajoutés avec succès !")

'''create_service()
insert_services()
create_employe()
add_employe() => used once'''

def get_employes_services():
    query = """
    SELECT employe.nom, employe.prenom, service.nom AS service
    FROM employe
    JOIN service ON employe.id_service = service.id
    """
    
    cur.execute(query)
    results = cur.fetchall()
    
    for row in results:
        print(f"{row[1]} { row[0]} travaille au service {row[2]}")

get_employes_services()

cur.close()
db.close()