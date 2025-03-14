import customtkinter as ctk
from database import Database

class AddProductForm(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Product")
        self.geometry("400x300")

        self.db = Database()
        self.categories = self.db.fetch_categories()

        ctk.CTkLabel(self, text="Product Name:").pack(pady=5)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)

        ctk.CTkLabel(self, text="Description:").pack(pady=5)
        self.desc_entry = ctk.CTkEntry(self)
        self.desc_entry.pack(pady=5)

        ctk.CTkLabel(self, text="Price (€):").pack(pady=5)
        self.price_entry = ctk.CTkEntry(self)
        self.price_entry.pack(pady=5)

        ctk.CTkLabel(self, text="Quantity:").pack(pady=5)
        self.qty_entry = ctk.CTkEntry(self)
        self.qty_entry.pack(pady=5)

        ctk.CTkLabel(self, text="Category:").pack(pady=5)
        self.category_var = ctk.StringVar()
        self.category_dropdown = ctk.CTkComboBox(self, variable=self.category_var, values=[cat[1] for cat in self.categories])
        self.category_dropdown.pack(pady=5)

        self.submit_button = ctk.CTkButton(self, text="Add", command=self.add_product)
        self.submit_button.pack(pady=10)

    def add_product(self):
        """Ajoute le produit à la base de données."""
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        price = self.price_entry.get()
        qty = self.qty_entry.get()
        category_name = self.category_var.get()

        if name and desc and price and qty and category_name:
            # Trouver l'ID de la catégorie sélectionnée
            category_id = next((cat[0] for cat in self.categories if cat[1] == category_name), None)
            if category_id:
                self.db.cur.execute(
                    "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                    (name, desc, price, qty, category_id),
                )
                self.db.db.commit()

        self.db.close()
        self.destroy()
