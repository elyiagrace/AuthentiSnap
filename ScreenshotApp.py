from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QRubberBand
from PyQt5.QtGui import QPixmap, QMouseEvent, QGuiApplication
from PyQt5.QtCore import QRect, QPoint, QSize, Qt
from PIL import Image
import pyautogui
import time

# This function takes a screenshot of the specified area
def take_screenshot(rect):
    screenshot = pyautogui.screenshot(region=(rect.x(), rect.y(), rect.width(), rect.height()))
    save_path, _ = QFileDialog.getSaveFileName(None, "Save Screenshot", "", "PNG Files (*.png);;All Files (*)")
    if save_path:
        screenshot.save(save_path)
        return save_path
    return None

# Main Window Class
class ScreenshotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot App")
        self.setGeometry(100, 100, 600, 400)  # Resizable window size

        # Set up the layout and button to trigger the screenshot selection
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        # Button to start screenshot selection
        self.button = QPushButton('Select Area and Take Screenshot')
        self.button.clicked.connect(self.select_area)
        self.layout.addWidget(self.button)

        # Label to display the screenshot
        self.label = QLabel('Screenshot will appear here')
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def select_area(self):
        # Hide the main window before starting the selection process
        self.hide()

        # Create an instance of the selection window
        self.selection_window = SelectionWindow(self)
        self.selection_window.showFullScreen()

    def show_screenshot(self, screenshot_path):
        # Show the main window again and display the captured screenshot
        self.show()
        if screenshot_path:
            pixmap = QPixmap(screenshot_path)
            self.label.setPixmap(pixmap)  # Display image in its original size
    # Class for the overlay window where the user selects the area
class SelectionWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setWindowOpacity(0.3)
        self.setStyleSheet("background-color: black;")
        self.rubber_band = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        self.origin = event.pos()
        self.rubber_band.setGeometry(QRect(self.origin, QSize()))
        self.rubber_band.show()

    def mouseMoveEvent(self, event: QMouseEvent):
        self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event: QMouseEvent):
        selected_rect = self.rubber_band.geometry()
        self.rubber_band.hide()

        # Take the screenshot of the selected area
        screenshot_path = take_screenshot(selected_rect)

        # Close the selection window and show the main window with the screenshot
        self.close()
        self.main_app.show_screenshot(screenshot_path)
