from domain.exceptions.invalid_password import InvalidPasswordError
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from infrastructure.security.argon2_password_hasher import Argon2PasswordHasher
from application.use_cases.register_user import RegisterUser
from application.use_cases.login_user import LoginUser
from domain.validators.username_validator import UsernameValidator
from domain.validators.email_validator import EmailValidator
from domain.validators.password_validator import PasswordValidator


def create_login_user_with_registered_user():
    repository = InMemoryUserRepository()
    hasher = Argon2PasswordHasher()

    register_use_case = RegisterUser(
        username_validator=UsernameValidator,
        email_validator=EmailValidator,
        password_validator=PasswordValidator,
        password_hasher=hasher,
        user_repository=repository,
    )

    login_use_case = LoginUser(
        user_repository=repository,
        password_hasher=hasher,
    )

    registered_user = register_use_case.execute(
        username="Yuri_dev",
        display_name="Yuri",
        email="yuri@email.com",
        password="Senha123!",
    )

    return login_use_case, registered_user


def test_login_successfully():
    login_use_case, registered_user = create_login_user_with_registered_user()

    user = login_use_case.execute("Yuri_dev", "Senha123!")

    assert user.id == registered_user.id
    assert user.username == "Yuri_dev"


def test_login_raises_when_user_not_found():
    login_use_case, _ = create_login_user_with_registered_user()

    with pytest.raises(InvalidPasswordError):
        login_use_case.execute("usuario_inexistente", "Senha123!")


def test_login_raises_with_wrong_password():
    login_use_case, _ = create_login_user_with_registered_user()

    with pytest.raises(InvalidPasswordError):
        login_use_case.execute("Yuri_dev", "SenhaErrada123!")


import pytest
