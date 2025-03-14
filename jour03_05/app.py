import sys
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

app = QApplication(sys.argv)
os.environ["QT_PLUGIN_PATH"] = r"C:\\Users\\porta\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\PyQt6\\Qt6\\plugins\\sqldrivers"

# os.add_dll_directory(r"C:\\Program Files\\MySQL\\MySQL Connector C 8.0\\lib")
# List possible MySQL paths (change these based on what you find)
possible_paths = [
    r"C:\\Program Files\\MySQL\\MySQL Connector C 8.0\\lib",
    r"C:\\Program Files\\MySQL\\MySQL Connector C++ 8.0\\lib64",
    r"C:\\Program Files\\MySQL\\Connector C++ 8.0\\lib",
]

# Automatically find the correct MySQL library path
for path in possible_paths:
    if os.path.exists(path):
        print(f"✅ Found MySQL library folder: {path}")
        os.add_dll_directory(path)  # Load the library dynamically
        break
else:
    print("❌ Error: MySQL library folder not found! Check your installation.")


print("Available drivers:", QSqlDatabase.drivers())  # Must be after QApplication
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

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My store's stock manager")
        self.setGeometry(100, 100, 800, 500)
        
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setPort(3306)
        self.db.setDatabaseName("store")
        self.db.setUserName(USER)
        self.db.setPassword(PASS)
        
        if not self.db.open():
            print("Error: Failed to connect to the database")
            return

w = MainWindow()
w.show()
app.exec()