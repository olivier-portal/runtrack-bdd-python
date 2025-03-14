import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

# Charger les variables d'environnement
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Récupérer les informations de connexion depuis .env
USER = os.getenv("USER")
PASS = os.getenv("PASS")

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=USER,
            password=PASS,
            database="store"
        )
        self.cur = self.db.cursor()

    def fetch_categories(self):
        """Get all categories"""
        self.cur.execute("SELECT * FROM category")
        return self.cur.fetchall()

    def fetch_products(self):
        """Get all products"""
        self.cur.execute("SELECT * FROM product")
        return self.cur.fetchall()
    
    def fetch_products_and_categories(self):
        """Get products and their category"""
        query = """
            SELECT product.id_product, product.name, product.description, product.price, category.name 
            FROM product
            LEFT JOIN category ON product.id_category = category.id_category
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def close(self):
        """Close db"""
        self.cur.close()
        self.db.close()
