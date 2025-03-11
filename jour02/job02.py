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

# Execute a query
cur.execute("CREATE TABLE etage (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nom VARCHAR(255) NOT NULL, numero INT NOT NULL, superficie INT NOT NULL)")

cur.execute("CREATE TABLE salle (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nom VARCHAR(255) NOT NULL, id_etage INT NOT NULL, capacite INT NOT NULL)")

cur.close()
db.close()