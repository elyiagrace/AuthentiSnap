# ui.py

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont, QColor, QFontDatabase
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from snipping_tool import SnippingTool

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)  # Increased height for better spacing
        self.setStyleSheet("background-color: #2c3e50;")  # Custom background color for title bar

        # Layout for the custom title bar
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 10, 0)  # Add padding to the left and right

        # Title Label
        self.title_label = QLabel("AuthentSnap")
        self.title_label.setStyleSheet("""
            color: white;
            font-size: 24px;  # Increase font size
            font-weight: 600;  # Make font bolder
            padding: 10px;  # Add padding around the text for better legibility
        """)
        layout.addWidget(self.title_label)

        # Add buttons (minimize, close)
        self.minimize_button = QPushButton("-")
        self.minimize_button.setFixedSize(40, 30)
        self.minimize_button.setStyleSheet("background-color: #3498db; color: white; border: none;")
        self.minimize_button.clicked.connect(self.minimize_window)
        layout.addWidget(self.minimize_button)

        self.close_button = QPushButton("x")
        self.close_button.setFixedSize(40, 30)
        self.close_button.setStyleSheet("background-color: #e74c3c; color: white; border: none;")
        self.close_button.clicked.connect(self.close_window)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def minimize_window(self):
        """Minimize the window"""
        self.window().showMinimized()

    def close_window(self):
        """Close the window"""
        self.window().close()

    # Make the window draggable by clicking on the title bar
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.window().move(event.globalPos() - self.drag_position)
            event.accept()


class WelcomeScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove the title bar
        self.setGeometry(300, 200, 500, 400)  # Window size and position

        # Apply gradient background
        self.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #232526, stop:1 #414345);")
        
        # Main layout for the window
        layout = QVBoxLayout()

        # Add custom title bar
        self.custom_title_bar = CustomTitleBar(self)
        layout.addWidget(self.custom_title_bar)

        # Set a modern font for the welcome message
        self.apply_modern_font()

        # Welcome message label
        welcome_message = QLabel("Welcome to AuthentSnap!")
        welcome_message.setAlignment(Qt.AlignCenter)
        welcome_message.setStyleSheet("color: white;")
        welcome_message.setFont(QFont("Montserrat", 18, QFont.Bold))  # Modern Font
        welcome_message.setWordWrap(True)

        # Add shadow effect to the welcome message
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(QColor(0, 0, 0, 160))
        shadow_effect.setOffset(4, 4)
        welcome_message.setGraphicsEffect(shadow_effect)

        layout.addWidget(welcome_message)

        # Add the start button with rounded corners and hover effect
        start_button = QPushButton("Start Snipping")
        start_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        start_button.setFixedWidth(200)
        start_button.setFixedHeight(50)

        # Add animation for the button (simple fade-in effect)
        self.button_animation = QPropertyAnimation(start_button, b"geometry")
        self.button_animation.setDuration(1000)  # 1 second duration
        self.button_animation.setStartValue(QRect(150, 300, 0, 0))
        self.button_animation.setEndValue(QRect(150, 300, 200, 50))

        # Connect the button click to start the snipping tool
        start_button.clicked.connect(self.start_snipping)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Run the animation
        self.button_animation.start()

    def apply_modern_font(self):
        """Apply a modern font for the welcome message (if available)."""
        # Try to load the 'Montserrat' font (or any other modern font)
        QFontDatabase.addApplicationFont("font/Montserrat-Regular.ttf")  # Make sure you have this font in the 'font/' folder

    def start_snipping(self):
        """Start the SnippingTool after clicking the Start button."""
        self.close()
        self.snipping_tool = SnippingTool()
        self.snipping_tool.show()

    # Make the window draggable from any point in the window (not just the custom title bar)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
