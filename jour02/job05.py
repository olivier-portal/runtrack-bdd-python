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

# Query to calculate total superficy from etage
cur.execute("SELECT SUM(superficie) FROM etage")

result = cur.fetchone()[0]

print(f"La superficie de La Plateforme est de {result} m²")

cur.close()
db.close()