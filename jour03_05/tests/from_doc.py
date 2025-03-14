import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction

'''
the QMainWindow is a pre-made widget which provides a lot of standard window features you'll make use of in your apps, including toolbars, menus, a statusbar, dockable widgets and more.
The best approach is to subclass QMainWindow and then include the setup for the window in the __init__ block. This allows the window behavior to be self contained. We can add our own subclass of QMainWindow — call it MainWindow to keep things simple.
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My store manager app")
        self.setMinimumSize(QSize(600, 450))
        
        layout = QVBoxLayout()
        
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
        
        for w in widgets:
            layout.addWidget(w())
            
        widget = QWidget()
        widget.setLayout(layout)
        
    #     self.label = QLabel("Click in this window")
    #     self.setCentralWidget(self.label)

    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouseMoveEvent")

    # def mousePressEvent(self, e):
    #     self.label.setText("mousePressEvent")

    # def mouseReleaseEvent(self, e):
    #     self.label.setText("mouseReleaseEvent")

    # def mouseDoubleClickEvent(self, e):
    #     self.label.setText("mouseDoubleClickEvent")
        
        # self.label = QLabel()
        
        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)
        
        # container = QWidget()
        # container.setLayout(layout)
        
        self.setCentralWidget(widget)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()