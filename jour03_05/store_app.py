import customtkinter as ctk
from database import Database
from add_category_form import AddCategoryForm
from add_product_form import AddProductForm

# Init CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class StoreApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Store Management")
        self.geometry("600x400")
        self.minsize(600, 450)

        # Connexion to database
        self.db = Database()

        # UI Elements
        self.label = ctk.CTkLabel(self, text="List of products", font=("Arial", 20))
        self.label.pack(pady=10)

        # List of products with checkboxes
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=650, height=300)
        self.scrollable_frame.pack(pady=10, fill = "both", expand = True)
        
        # store checboxes in a dictionary
        self.product_checkboxes = {}

        # Load automatically all products list
        self.load_products()
        
        # add buttons to add products or categories
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(side="bottom", fill="x", pady=10)
        
        self.add_category_button = ctk.CTkButton(button_frame, text="Add Category", command = self.open_add_category)
        self.add_category_button.pack(side="left", padx=10, pady=5, expand=True)
        
        self.add_product_button = ctk.CTkButton(button_frame, text="Add Product", command = self.open_add_product)
        self.add_product_button.pack(side="right", padx=10, pady=5, expand=True)

    def load_products(self):
        """Load products with checkboxes"""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()  # Suppress old widgets

        products = self.db.fetch_products_and_categories()

        for product in products:
            product_id, name, description, price, category = product
            var = ctk.StringVar()
            checkbox = ctk.CTkCheckBox(self.scrollable_frame, text=f"{name} - {description} - {price}€ - {category}", variable=var)
            checkbox.pack(anchor="w", padx=10, pady=2)
            self.product_checkboxes[product_id] = var
            
    def open_add_category(self):
        """Open category window"""
        AddCategoryForm(self)

    def open_add_product(self):
        """Open product window"""
        AddProductForm(self)

    def on_close(self):
        """Close connexion to db"""
        self.db.close()
        self.destroy()

# Launch app
if __name__ == "__main__":
    app = StoreApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
