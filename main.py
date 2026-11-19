"""
main.py
Application entry point for Seyes Editor.
"""

import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont, QIcon, QGuiApplication
from PyQt6.QtCore import Qt

from seyes_engine import TypographyEngine
from ui import MainWindow


def main():
    # Enable crisp High-DPI rendering for modern Windows displays (100%, 125%, 150%, 200%)
    if hasattr(QGuiApplication, 'setHighDpiScaleFactorRoundingPolicy'):
        QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )
    if hasattr(Qt.ApplicationAttribute, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    if hasattr(Qt.ApplicationAttribute, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("Seyes Editor")
    app.setApplicationDisplayName("Seyes Editor")
    app.setOrganizationName("SeyesEditor")

    if getattr(sys, 'frozen', False):
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Set Application Icon
    icon_path = os.path.join(base_dir, "assets", "icon.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    # Set modern clean application font
    app.setFont(QFont("Segoe UI", 10))

    # Resolve fonts path
    fonts_dir = os.path.join(base_dir, "assets", "fonts")

    # Load bundled educational fonts
    TypographyEngine.load_font_assets(fonts_dir)

    # Launch main window with screen-adaptive window sizing
    window = MainWindow(fonts_dir=fonts_dir)
    screen = QApplication.primaryScreen()
    if screen:
        avail = screen.availableGeometry()
        if avail.width() <= 1440 or avail.height() <= 900:
            window.showMaximized()
        else:
            window.show()
    else:
        window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
