import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.styles.theme import Theme


def create_app():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    app.setStyle("Fusion")

    palette = app.palette()
    from ui.styles.colors import Colors
    palette.setColor(palette.ColorRole.Base, QColor(Colors.background))
    palette.setColor(palette.ColorRole.Window, QColor(Colors.background))
    palette.setColor(palette.ColorRole.Text, QColor(Colors.on_surface))
    palette.setColor(palette.ColorRole.WindowText, QColor(Colors.on_surface))
    app.setPalette(palette)

    return app


def main():
    app = create_app()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
