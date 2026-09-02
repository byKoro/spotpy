from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox,
    QSpacerItem, QSizePolicy, QMessageBox,
)
from ui.styles.colors import Colors
from ui.styles.fonts import Fonts
from ui.styles.theme import Theme
from ui.components.fields import InputField, PasswordField, PrimaryButton

class LoginScreen(QWidget):

    login_success = Signal(object)
    register_requested = Signal()

    def __init__(self, login_use_case, parent=None):
        super().__init__(parent)
        self._login_use_case = login_use_case
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)

        container = QWidget()
        container.setMinimumWidth(400)
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        container.setStyleSheet(f"""
            QWidget {{
                background-color: {Colors.surface_container_high};
                border-radius: 8px;
            }}
            """)
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(40, 40, 40, 40)
        container_layout.setSpacing(32)

        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)

        title = QLabel("Spotipy")
        title.setFont(Theme.get_font(Fonts.display_lg_size, Fonts.display_lg_weight))
        title.setStyleSheet(f"color: {Colors.primary};")
        title.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title)

        subtitle = QLabel("Entrar no Spotipy")
        subtitle.setFont(Theme.get_font(Fonts.headline_md_size, Fonts.headline_md_weight))
        subtitle.setPalette(self._palette(Colors.on_surface))
        subtitle.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(subtitle)

        container_layout.addLayout(header_layout)

        form_layout = QVBoxLayout()
        form_layout.setSpacing(16)

        self.username_field = InputField(
            placeholder="E-mail ou nome de usuário",
            label_text="E-mail ou nome de usuário",
        )
        form_layout.addWidget(self.username_field)

        self.password_field = PasswordField(
            placeholder="Senha",
            label_text="Senha",
        )
        form_layout.addWidget(self.password_field)

        remember_layout = QHBoxLayout()
        remember_layout.setContentsMargins(0, 0, 0, 0)

        self.remember_checkbox = QCheckBox("Lembrar de mim")
        self.remember_checkbox.setFont(Theme.get_font(Fonts.body_md_size, Fonts.body_md_weight))
        self.remember_checkbox.setPalette(self._palette(Colors.on_surface))
        remember_layout.addWidget(self.remember_checkbox)

        remember_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        container_layout.addLayout(form_layout)
        container_layout.addLayout(remember_layout)

        self.login_button = PrimaryButton("Entrar")
        self.login_button.apply_style(
            bg_color=Colors.primary,
            text_color="#000000",
        )
        self.login_button.setMinimumHeight(48)
        self.login_button.setFont(Theme.get_font(Fonts.label_md_size, Fonts.label_md_weight))
        self.login_button.setCursor(Qt.PointingHandCursor)
        self.login_button.clicked.connect(self._on_login_clicked)
        container_layout.addWidget(self.login_button)

        links_layout = QVBoxLayout()
        links_layout.setSpacing(16)
        links_layout.setContentsMargins(0, 0, 0, 0)

        forgot_color = Colors.on_surface
        forgot_link = QLabel(
            f'<a href="#" style="color: {forgot_color}; text-decoration: none;">Esqueceu sua senha?</a>'
        )
        forgot_link.setTextFormat(Qt.RichText)
        forgot_link.setCursor(Qt.PointingHandCursor)
        forgot_link.setAlignment(Qt.AlignCenter)
        forgot_link.linkActivated.connect(lambda: self._on_link_clicked("forgot_password"))
        links_layout.addWidget(forgot_link)

        divider = QLabel()
        divider.setStyleSheet(f"background-color: {Colors.secondary_container};")
        divider.setFixedHeight(1)
        links_layout.addWidget(divider)

        signup_layout = QHBoxLayout()
        signup_layout.setSpacing(4)
        signup_layout.setContentsMargins(0, 0, 0, 0)
        signup_layout.setAlignment(Qt.AlignCenter)

        signup_label = QLabel("Não tem uma conta?")
        signup_label.setFont(Theme.get_font(Fonts.body_md_size, Fonts.body_md_weight))
        signup_label.setPalette(self._palette(Colors.on_surface_variant))
        signup_layout.addWidget(signup_label)

        signup_link = QLabel(
            f'<a href="#" style="color: {Colors.primary}; font-weight: 600; text-decoration: none;">Inscrever-se no Spotipy</a>'
        )
        signup_link.setTextFormat(Qt.RichText)
        signup_link.setCursor(Qt.PointingHandCursor)
        signup_link.linkActivated.connect(lambda: self._on_link_clicked("register"))
        signup_layout.addWidget(signup_link)

        links_layout.addLayout(signup_layout)

        container_layout.addLayout(links_layout)
        container_layout.addItem(
            QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
        layout.addWidget(container)
        layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

    @staticmethod
    def _palette(text_color):
        p = QPalette()
        p.setColor(QPalette.ColorRole.WindowText, QColor(text_color))
        p.setColor(QPalette.ColorRole.Text, QColor(text_color))
        return p

    def _on_login_clicked(self):
        username = self.username_field.text()
        password = self.password_field.text()

        try:
            user = self._login_use_case.execute(username, password)
            self.login_success.emit(user)
        except Exception as e:
            self._show_error(str(e))

    def _on_link_clicked(self, link):
        if link == "register":
            self.register_requested.emit()

    def _show_error(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Erro de Login")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
