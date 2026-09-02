from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.styles.theme import Theme
from ui.screens.login_screen import LoginScreen
from ui.screens.register_screen import RegisterScreen
from application.use_cases.login_user import LoginUser
from application.use_cases.register_user import RegisterUser
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from infrastructure.security.argon2_password_hasher import Argon2PasswordHasher
from domain.validators.username_validator import UsernameValidator
from domain.validators.email_validator import EmailValidator
from domain.validators.password_validator import PasswordValidator


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotipy")
        self.resize(734, 800)

        self._setup_dependencies()
        self._setup_ui()

    def _setup_dependencies(self):
        self.user_repository = InMemoryUserRepository()
        self.password_hasher = Argon2PasswordHasher()

        self.login_use_case = LoginUser(
            user_repository=self.user_repository,
            password_hasher=self.password_hasher,
        )

        self.register_use_case = RegisterUser(
            username_validator=UsernameValidator,
            email_validator=EmailValidator,
            password_validator=PasswordValidator,
            password_hasher=self.password_hasher,
            user_repository=self.user_repository,
        )

    def _setup_ui(self):
        self.setStyleSheet(Theme.get_app_stylesheet())
        self._show_login_screen()

    def _show_login_screen(self):
        self.login_screen = LoginScreen(self.login_use_case)
        self.login_screen.login_success.connect(self._on_login_success)
        self.login_screen.register_requested.connect(self._show_register_screen)
        self.setCentralWidget(self.login_screen)

    def _show_register_screen(self):
        self.register_screen = RegisterScreen(
            self.register_use_case,
            self.login_use_case,
        )
        self.register_screen.login_requested.connect(self._show_login_screen)
        self.register_screen.register_success.connect(self._on_register_success)
        self.setCentralWidget(self.register_screen)

    def _on_login_success(self, user):
        msg = QMessageBox()
        msg.setWindowTitle("Login Bem-sucedido")
        msg.setText(f"Bem-vindo, {user.display_name}!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def _on_register_success(self, user):
        msg = QMessageBox()
        msg.setWindowTitle("Registro Bem-sucedido")
        msg.setText(f"Conta criada para {user.username}! Faça login.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
        self._show_login_screen()
