from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QSpacerItem, QSizePolicy, QMessageBox,
)
from ui.styles.colors import Colors
from ui.styles.fonts import Fonts
from ui.styles.theme import Theme
from ui.components.fields import InputField, PasswordField, PrimaryButton


class RegisterScreen(QWidget):

    register_success = Signal(object)
    login_requested = Signal()

    def __init__(self, register_use_case, login_use_case, parent=None):
        super().__init__(parent)
        self._register_use_case = register_use_case
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
        container_layout.setSpacing(24)

        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)

        title = QLabel("Spotipy")
        title.setFont(Theme.get_font(Fonts.display_lg_size, Fonts.display_lg_weight))
        title.setStyleSheet(f"color: {Colors.primary};")
        title.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title)

        subtitle = QLabel("Criar conta no Spotipy")
        subtitle.setFont(Theme.get_font(Fonts.headline_md_size, Fonts.headline_md_weight))
        subtitle.setPalette(self._palette(Colors.on_surface))
        subtitle.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(subtitle)

        container_layout.addLayout(header_layout)

        form_layout = QVBoxLayout()
        form_layout.setSpacing(16)

        self.username_field = InputField(
            placeholder="Nome de usuário",
            label_text="Nome de usuário",
        )
        form_layout.addWidget(self.username_field)

        self.display_name_field = InputField(
            placeholder="Nome completo",
            label_text="Nome completo",
        )
        form_layout.addWidget(self.display_name_field)

        self.email_field = InputField(
            placeholder="E-mail",
            label_text="E-mail",
        )
        form_layout.addWidget(self.email_field)

        self.password_field = PasswordField(
            placeholder="Senha",
            label_text="Senha",
        )
        form_layout.addWidget(self.password_field)

        container_layout.addLayout(form_layout)

        self.register_button = PrimaryButton("Criar conta")
        self.register_button.apply_style(
            bg_color=Colors.primary,
            text_color="#000000",
        )
        self.register_button.setMinimumHeight(48)
        self.register_button.setFont(Theme.get_font(Fonts.label_md_size, Fonts.label_md_weight))
        self.register_button.setCursor(Qt.PointingHandCursor)
        self.register_button.clicked.connect(self._on_register_clicked)
        container_layout.addWidget(self.register_button)

        links_layout = QVBoxLayout()
        links_layout.setSpacing(16)
        links_layout.setContentsMargins(0, 0, 0, 0)

        divider = QLabel()
        divider.setStyleSheet(f"background-color: {Colors.secondary_container};")
        divider.setFixedHeight(1)
        links_layout.addWidget(divider)

        login_layout = QHBoxLayout()
        login_layout.setSpacing(2)
        login_layout.setContentsMargins(0, 0, 0, 0)
        login_layout.setAlignment(Qt.AlignCenter)

        login_label = QLabel("Já tem uma conta?")
        login_label.setFont(Theme.get_font(Fonts.body_md_size, Fonts.body_md_weight))
        login_label.setPalette(self._palette(Colors.on_surface_variant))
        login_layout.addWidget(login_label)

        login_link = QLabel(
            f'<a href="#" style="color: {Colors.primary}; font-weight: 600; text-decoration: none;">Entrar</a>'
        )
        login_link.setTextFormat(Qt.RichText)
        login_link.setCursor(Qt.PointingHandCursor)
        login_link.linkActivated.connect(self._on_login_link_clicked)
        login_layout.addWidget(login_link)

        links_layout.addLayout(login_layout)
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

    def _on_register_clicked(self):
        username = self.username_field.text()
        display_name = self.display_name_field.text()
        email = self.email_field.text()
        password = self.password_field.text()

        if not username or not display_name or not email or not password:
            self._show_error("Todos os campos são obrigatórios.")
            return

        try:
            user = self._register_use_case.execute(
                username=username,
                display_name=display_name,
                email=email,
                password=password,
            )
            self.register_success.emit(user)
        except Exception as e:
            self._show_error(str(e))

    def _on_login_link_clicked(self):
        self.login_requested.emit()

    def _show_error(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Erro no Registro")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
