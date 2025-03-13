import sys
import os

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
        
        toolbar =QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        # Ensure correct path to the icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "assets", "icons", "folder-open.png")

        # Debugging
        # print(f"Resolved icon path: {icon_path}, Exists: {os.path.exists(icon_path)}")
        
        button_action = QAction(QIcon(icon_path), "Button1", self)
        button_action.setStatusTip("This is a button")
        button_action.triggered.connect(self.on_toolbar_click)
        button_action.setCheckable(True)
        
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)
        
        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon(icon_path), "Button2", self)
        button_action2.setStatusTip("This is a button")
        button_action2.triggered.connect(self.on_toolbar_click)
        button_action.setCheckable(True)
        toolbar.addAction(button_action2)
        
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
               
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action)
        file_submenu.addSeparator
        file_submenu.addAction(button_action2)
        
    def on_toolbar_click(self, s):
        print("clicked", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()