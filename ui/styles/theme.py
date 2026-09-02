from PySide6.QtGui import QFont
from ui.styles.colors import Colors
from ui.styles.fonts import Fonts


class Theme:

    colors = Colors
    fonts = Fonts

    @staticmethod
    def get_font(size, weight, family=Fonts.body_family):
        font = QFont(family)
        font.setPixelSize(size)
        font.setWeight(QFont.Weight(weight))
        return font

    @staticmethod
    def get_app_stylesheet():
        return f"""
QWidget {{
    background-color: {Colors.background};
    color: {Colors.on_surface};
    font-family: '{Fonts.body_family}';
}}

QLabel {{
    color: {Colors.on_surface};
}}

QPushButton {{
    border: none;
    background: transparent;
    color: {Colors.on_surface};
    font-family: '{Fonts.body_family}';
}}

QPushButton:hover {{
    color: {Colors.primary};
}}

QLineEdit {{
    background-color: {Colors.input_bg};
    border: 1px solid {Colors.input_border};
    border-radius: 4px;
    padding: 8px 12px;
    color: {Colors.on_surface};
    font-family: '{Fonts.body_family}';
    selection-background-color: {Colors.primary};
}}

QLineEdit:focus {{
    border: 1px solid {Colors.on_surface};
    border-radius: 4px;
}}

QCheckBox {{
    color: {Colors.on_surface};
    font-family: '{Fonts.body_family}';
}}

QCheckBox::indicator {{
    width: 16px;
    height: 16px;
    border: 1px solid {Colors.input_border};
    border-radius: 3px;
    background-color: {Colors.input_bg};
}}

QCheckBox::indicator:checked {{
    background-color: {Colors.primary};
    border: 1px solid {Colors.primary};
}}

QScrollBar:vertical {{
    border: none;
    background: transparent;
    width: 8px;
    margin: 0px;
}}

QScrollBar::handle:vertical {{
    background: {Colors.outline};
    border-radius: 4px;
}}

QDialog {{
    background-color: {Colors.surface};
}}
"""
