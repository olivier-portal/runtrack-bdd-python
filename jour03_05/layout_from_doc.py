import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget
from PyQt6.QtCore import QSize

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(600, 450))
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)
        
        #--------------------------------------------------
        
        # layout = QGridLayout()

        # layout.addWidget(Color("red"), 0, 3)
        # layout.addWidget(Color("green"), 1, 1)
        # layout.addWidget(Color("orange"), 2, 2)
        # layout.addWidget(Color("blue"), 3, 0)

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)
        
        # layout1 = QHBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()

        # layout2.addWidget(Color("red"))
        # layout2.addWidget(Color("yellow"))
        # layout2.addWidget(Color("purple"))

        # layout1.setContentsMargins(0,0,0,0)
        # layout1.setSpacing(20)

        # layout1.addLayout(layout2)

        # layout1.addWidget(Color("green"))

        # layout3.addWidget(Color("red"))
        # layout3.addWidget(Color("purple"))

        # layout1.addLayout(layout3)

        # widget = QWidget()
        # widget.setLayout(layout1)
        # self.setCentralWidget(widget)
        
        #--------------------------------------------------

        # layout = QVBoxLayout()

        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("orange"))
        # layout.addWidget(Color("blue"))

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)
        
        # layout.setContentsMargins(0,0,0,0)
        # layout.setSpacing(0)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()