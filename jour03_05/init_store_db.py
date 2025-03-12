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
    database="store" # added after database creation
    )

# Get a cursor
cur = db.cursor()

# create databasebefore adding database in db
# cur.execute("CREATE DATABASE store")

class Store:
    def __init__(self):      
        cur.execute("USE store")
        
    # Create tables category and product
    def create_category(self):
        cur.execute("CREATE TABLE IF NOT EXISTS category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL)")
        db.commit()
        print("Table 'category' successfully created !")
        
    def create_product(self):
        cur.execute("CREATE TABLE IF NOT EXISTS product (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, price INT NOT NULL, quantity INT NOT NULL, id_category INT NOT NULL)")
        db.commit()
        print("Table 'product' successfully created !")
        
    def insert_categories(self):
        sql = "INSERT INTO category (name) VALUES (%s)"
        val = [
        ('T-Shirts',),
        ('Jeans',),
        ('Jackets',),
        ('Sweaters',),
        ('Accessories',)
        ]

        cur.executemany(sql, val)

        db.commit()

        print(cur.rowcount, "was inserted.")
        
    def insert_products(self):
        sql = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        val = [
        ('Basic White T-Shirt', 'A simple and classic white t-shirt', 15, 100, 1),
        ('Graphic T-Shirt', 'A t-shirt with a cool graphic print', 20, 50, 1),
        ('V-Neck T-Shirt', 'A comfortable v-neck t-shirt', 18, 80, 1),
        ('Striped T-Shirt', 'T-shirt with horizontal stripes', 17, 70, 1),
        ('Oversized T-Shirt', 'A trendy oversized t-shirt', 25, 40, 1),
        
        ('Black Skinny Jeans', 'Slim fit black jeans', 40, 120, 2),
        ('Blue Denim Jeans', 'Classic blue denim jeans', 45, 80, 2),
        ('Ripped Jeans', 'Jeans with a distressed, ripped look', 50, 60, 2),
        ('Bootcut Jeans', 'Flared bootcut jeans for a vintage look', 55, 100, 2),
        ('High-Waisted Jeans', 'High-waisted jeans with a modern fit', 48, 90, 2),
        
        ('Leather Jacket', 'Black leather jacket for an edgy style', 150, 40, 3),
        ('Denim Jacket', 'Casual denim jacket with buttoned closure', 80, 60, 3),
        ('Bomber Jacket', 'Stylish bomber jacket in olive green', 100, 50, 3),
        ('Blazer Jacket', 'Formal blazer jacket for business style', 120, 30, 3),
        ('Puffer Jacket', 'Puffy jacket perfect for winter', 130, 70, 3),
        
        ('Grey Wool Sweater', 'Warm and soft grey wool sweater', 60, 110, 4),
        ('Cashmere Sweater', 'Luxurious soft cashmere sweater', 120, 40, 4),
        ('V-Neck Sweater', 'Classic v-neck sweater in various colors', 55, 60, 4),
        ('Chunky Knit Sweater', 'Cozy and oversized chunky knit sweater', 70, 80, 4),
        ('Striped Sweater', 'Sweater with stylish stripes across', 65, 50, 4),
        
        ('Sunglasses', 'Stylish round sunglasses for sunny days', 25, 150, 5),
        ('Leather Belt', 'Classic black leather belt', 30, 200, 5),
        ('Baseball Cap', 'Trendy baseball cap in various colors', 20, 120, 5),
        ('Scarf', 'Cozy scarf to keep you warm', 18, 130, 5),
        ('Watch', 'Elegant wristwatch with leather strap', 75, 90, 5)
        ]

        cur.executemany(sql, val)

        db.commit()

        print(cur.rowcount, "was inserted.")
        
# Create an instance for store's Class
store_instance = Store()

store_instance.create_category()
store_instance.create_product()
store_instance.insert_categories()
store_instance.insert_products()


cur.close()
db.close()