# welcome_screen.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QFont, QColor, QFontDatabase, QBrush, QPixmap, QPalette
from PyQt5.QtCore import Qt
from custom_title_bar import CustomTitleBar  # Import CustomTitleBar from custom_title_bar.py
from snipping_tool import SnippingTool
import os

class WelcomeScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(300, 200, 500, 400)

        # Set background image
        self.setAutoFillBackground(True)
        palette = QPalette()

        # Ensure the image path is correct
        image_path = os.path.join(os.path.dirname(__file__), "art-deco.jpg")  # Adjust path as needed
        background_brush = QBrush(QPixmap(image_path))

        palette.setBrush(QPalette.Window, background_brush)  # Use the QBrush
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.custom_title_bar = CustomTitleBar(self)
        layout.addWidget(self.custom_title_bar)

        self.apply_modern_font()

        # Welcome message label
        welcome_message = QLabel("Welcome to Authentihash!")
        welcome_message.setAlignment(Qt.AlignCenter)
        welcome_message.setStyleSheet("color: white;")
        welcome_message.setFont(QFont("Montserrat", 18, QFont.Bold))
        welcome_message.setWordWrap(True)

        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(QColor(0, 0, 0, 160))
        shadow_effect.setOffset(4, 4)
        welcome_message.setGraphicsEffect(shadow_effect)

        layout.addWidget(welcome_message)

        # Add the buttons for About and Snip
        about_button = QPushButton("About")
        snip_button = QPushButton("Snip")

        # Style for buttons
        button_style = """
            QPushButton {
                background-color: gold;  # Gold background
                color: black;  # Black text
                border: 2px solid darkred;  # Dark red border
                border-radius: 10px;  # Rounded corners
                padding: 10px 20px;  # Padding for button
                font-size: 16px;  # Font size
                font-weight: bold;  # Bold font
            }
            QPushButton:hover {
                background-color: darkred;  # Dark red hover effect
                color: white;  # Change text color on hover
            }
        """
        about_button.setStyleSheet(button_style)
        snip_button.setStyleSheet(button_style)

        layout.addWidget(about_button, alignment=Qt.AlignCenter)
        layout.addWidget(snip_button, alignment=Qt.AlignCenter)

        # Connect button signals
        about_button.clicked.connect(self.show_about)
        snip_button.clicked.connect(self.start_snipping)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def apply_modern_font(self):
        QFontDatabase.addApplicationFont("font/Montserrat-Regular.ttf")  # Ensure the font is available

    def show_about(self):
        # Show about information (implement your logic here)
        print("About clicked")  # Placeholder for actual implementation

    def start_snipping(self):
        self.close()
        self.snipping_tool = SnippingTool()
        self.snipping_tool.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
