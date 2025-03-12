import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtCore import QSize, Qt

'''
the QMainWindow is a pre-made widget which provides a lot of standard window features you'll make use of in your apps, including toolbars, menus, a statusbar, dockable widgets and more.
The best approach is to subclass QMainWindow and then include the setup for the window in the __init__ block. This allows the window behavior to be self contained. We can add our own subclass of QMainWindow — call it MainWindow to keep things simple.
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My store manager app")
        
        self.setMinimumSize(QSize(600, 450))

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()