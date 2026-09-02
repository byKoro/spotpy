from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QLabel
from PySide6.QtGui import QFont, QColor, QPalette
from ui.styles.colors import Colors
from ui.styles.fonts import Fonts
from ui.styles.theme import Theme


class PrimaryButton(QPushButton):

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(48)
        self.setMinimumWidth(100)
        font = Theme.get_font(Fonts.label_md_size, Fonts.label_md_weight)
        self.setFont(font)
        self.setCursor(Qt.PointingHandCursor)

    def apply_style(self, bg_color=Colors.primary, text_color="#000000", border_radius="9999px"):
        self.setStyleSheet(f"""
QPushButton {{
    background-color: {bg_color};
    color: {text_color};
    border-radius: {border_radius};
    padding: 8px 16px;
}}
QPushButton:hover {{
    background-color: #47d68c;
}}
QPushButton:pressed {{
    background-color: #2db86b;
}}
""")


class InputField(QWidget):

    text_changed = Signal(str)

    def __init__(self, placeholder="", label_text="", parent=None, echo_mode=QLineEdit.Normal):
        super().__init__(parent)
        self._build_ui(placeholder, label_text, echo_mode)

    def _build_ui(self, placeholder, label_text, echo_mode):
        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        if label_text:
            self.label = QLabel(label_text)
            self.label.setFont(Theme.get_font(Fonts.label_md_size, Fonts.label_md_weight))
            self.label.setStyleSheet(f"color: {Colors.on_surface_variant};")
            layout.addWidget(self.label)

        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)
        self.input.setEchoMode(echo_mode)
        self.input.setMinimumHeight(48)
        self.input.setFont(Theme.get_font(Fonts.body_md_size, Fonts.body_md_weight))

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Base, QColor(Colors.input_bg))
        palette.setColor(QPalette.ColorRole.Text, QColor(Colors.on_surface))
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(Colors.on_surface_variant))
        self.input.setPalette(palette)

        self.input.textChanged.connect(lambda: self.text_changed.emit(self.input.text()))
        layout.addWidget(self.input)

    def text(self):
        return self.input.text()

    def set_text(self, text):
        self.input.setText(text)

    def set_placeholder(self, placeholder):
        self.input.setPlaceholderText(placeholder)

    def set_echo_mode(self, mode):
        self.input.setEchoMode(mode)

    def set_label(self, text):
        if hasattr(self, 'label'):
            self.label.setText(text)


class PasswordField(QWidget):

    text_changed = Signal(str)

    def __init__(self, placeholder="", label_text="", parent=None):
        super().__init__(parent)
        self._is_visible = False
        self._build_ui(placeholder, label_text)

    def _build_ui(self, placeholder, label_text):
        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        if label_text:
            self.label = QLabel(label_text)
            self.label.setFont(Theme.get_font(Fonts.label_md_size, Fonts.label_md_weight))
            self.label.setStyleSheet(f"color: {Colors.on_surface_variant};")
            layout.addWidget(self.label)

        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)
        self.input.setEchoMode(QLineEdit.Password)
        self.input.setMinimumHeight(48)
        self.input.setFont(Theme.get_font(Fonts.body_md_size, Fonts.body_md_weight))

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Base, QColor(Colors.input_bg))
        palette.setColor(QPalette.ColorRole.Text, QColor(Colors.on_surface))
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(Colors.on_surface_variant))
        self.input.setPalette(palette)

        container = QWidget()
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.input)

        self.toggle_btn = QPushButton()
        self.toggle_btn.setFixedSize(40, 48)
        self.toggle_btn.setCursor(Qt.PointingHandCursor)
        self.toggle_btn.setStyleSheet("""
QPushButton {
    background: transparent;
    border: none;
    color: transparent;
}
""")
        self.toggle_btn.clicked.connect(self._toggle_visibility)
        container_layout.addWidget(self.toggle_btn)
        layout.addWidget(container)

    def _toggle_visibility(self):
        self._is_visible = not self._is_visible
        if self._is_visible:
            self.input.setEchoMode(QLineEdit.Normal)
        else:
            self.input.setEchoMode(QLineEdit.Password)

    @property
    def is_visible(self):
        return self._is_visible

    def text(self):
        return self.input.text()

    def set_text(self, text):
        self.input.setText(text)

    def set_placeholder(self, placeholder):
        self.input.setPlaceholderText(placeholder)
