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

# Query to get name and capacity from salle
query_salle = """
SELECT nom, capacite FROM salle;
"""
cur.execute(query_salle)

results = cur.fetchall()

print("List of name and capacities of rooms in salle: ")
for row in results:
    print(f"Name: {row[0]}, capacity: {row[1]}")

cur.close()
db.close()