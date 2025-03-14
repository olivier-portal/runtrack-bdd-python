import customtkinter as ctk
from database import Database

class AddCategoryForm(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Category")
        self.geometry("300x200")

        self.label = ctk.CTkLabel(self, text="Category Name:")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10)

        self.submit_button = ctk.CTkButton(self, text="Add", command=self.add_category)
        self.submit_button.pack(pady=10)

    def add_category(self):
        """Ajoute la catégorie à la base de données."""
        category_name = self.entry.get()
        if category_name:
            db = Database()
            db.cur.execute("INSERT INTO category (name) VALUES (%s)", (category_name,))
            db.db.commit()
            db.close()
            self.destroy()
