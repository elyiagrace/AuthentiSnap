# ui.py
# Image by <a href="https://www.freepik.com/free-vector/flat-design-art-deco-instagram-post-collection_20443444.htm#query=art%20deco&position=3&from_view=keyword&track=ais_hybrid&uuid=34d26661-f3e5-495b-beb1-b84826aa8189">Freepik</a>

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont, QColor, QFontDatabase
from PyQt5.QtCore import Qt
from custom_title_bar import CustomTitleBar  # Import CustomTitleBar from custom_title_bar.py
from snipping_tool import SnippingTool
from welcome_screen import WelcomeScreen  # Import the WelcomeScreen class

class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(300, 200, 500, 400)

        # Initialize WelcomeScreen
        self.welcome_screen = WelcomeScreen()
        self.welcome_screen.show()

    # Other methods can be added here for the main application functionality
