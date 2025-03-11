import mysql.connector

import os

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

# Query to add datas in etage
query_etage = """
INSERT INTO etage (nom, numero, superficie) 
VALUES 
('RDC', 0, 500), 
('R+1', 1, 500);
"""
cur.execute(query_etage)

# Query to add datas in salle
query_salle = """
INSERT INTO salle (nom, id_etage, capacite) 
VALUES 
('Lounge', 1, 100), 
('Studio Son', 1, 5), 
('Broadcasting', 2, 50), 
('Bocal Peda', 2, 4), 
('Coworking', 2, 80), 
('Studio Video', 2, 5);
"""
cur.execute(query_salle)

# Verify that datas have been added properly
cur.execute("SELECT * FROM etage")
print("Table 'etage':", cur.fetchall())

cur.execute("SELECT * FROM salle")
print("Table 'salle':", cur.fetchall())

db.commit()

cur.close()
db.close()

"""In terminal:
mysqldump -u olivier -p LaPlateforme > "C:\Users\porta\OneDrive\Documents\La plateforme\SQL\runtrack-bdd-python\jour02\etage.sql"
mysqldump -u olivier -p LaPlateforme > "C:\Users\porta\OneDrive\Documents\La plateforme\SQL\runtrack-bdd-python\jour02\salle.sql"
"""