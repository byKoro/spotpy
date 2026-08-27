from application.use_cases.register_user import RegisterUser
from infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository
)
from infrastructure.security.argon2_password_hasher import (
    Argon2PasswordHasher
)
from domain.validators.username_validator import UsernameValidator
from domain.validators.email_validator import EmailValidator
from domain.validators.password_validator import PasswordValidator
import pytest

def create_register_user():
    return RegisterUser(
        username_validator=UsernameValidator,
        email_validator=EmailValidator,
        password_validator=PasswordValidator,
        password_hasher=Argon2PasswordHasher(),
        user_repository=InMemoryUserRepository(),
    )


def test_register_user_successfully():

    register_user = create_register_user()

    user = register_user.execute(
        username="Yuri_dev",
        display_name="Yuri",
        email="yuri@email.com",
        password="Senha123!",
    )

    assert user.username == "Yuri_dev"
    assert user.display_name == "Yuri"
    assert user.email == "yuri@email.com"
    assert user.password_hash != "Senha123!"

def test_register_user_raises_when_username_already_exists():

    register_user = create_register_user()

    register_user.execute(
        username="Yuri_dev",
        display_name="Yuri",
        email="yuri@email.com",
        password="Senha123!",
    )

    from domain.exceptions.username_already_exists import (
        UsernameAlreadyExistsError
    )

    with pytest.raises(UsernameAlreadyExistsError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Outro Yuri",
            email="outro@email.com",
            password="Senha123!",
        )

def test_register_user_raises_when_email_already_exists():

    register_user = create_register_user()

    register_user.execute(
        username="Yuri_dev",
        display_name="Yuri",
        email="yuri@email.com",
        password="Senha123!",
    )

    from domain.exceptions.email_already_exists import (
        EmailAlreadyExistsError
    )

    with pytest.raises(EmailAlreadyExistsError):
        register_user.execute(
            username="Outro_usuario",
            display_name="Outro Yuri",
            email="yuri@email.com",
            password="Senha123!",
        )

def test_register_user_raises_when_email_already_exists():

    register_user = create_register_user()

    register_user.execute(
        username="Yuri_dev",
        display_name="Yuri",
        email="yuri@email.com",
        password="Senha123!",
    )

    from domain.exceptions.email_already_exists import (
        EmailAlreadyExistsError
    )

    with pytest.raises(EmailAlreadyExistsError):
        register_user.execute(
            username="Outro_usuario",
            display_name="Outro Yuri",
            email="yuri@email.com",
            password="Senha123!",
        )

def test_register_user_raises_when_username_is_invalid():

    register_user = create_register_user()

    from domain.exceptions.invalid_username import InvalidUsernameError

    with pytest.raises(InvalidUsernameError):
        register_user.execute(
            username="Yuri dev!",
            display_name="Yuri",
            email="yuri@email.com",
            password="Senha123!",
        )


def test_register_user_raises_when_username_is_too_long():

    register_user = create_register_user()

    from domain.exceptions.invalid_username import InvalidUsernameError

    with pytest.raises(InvalidUsernameError):
        register_user.execute(
            username="a" * 21,
            display_name="Yuri",
            email="yuri@email.com",
            password="Senha123!",
        )


def test_register_user_raises_when_email_is_invalid():

    register_user = create_register_user()

    from domain.exceptions.invalid_email import InvalidEmailError

    with pytest.raises(InvalidEmailError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Yuri",
            email="email_invalido",
            password="Senha123!",
        )


def test_register_user_raises_when_password_is_too_short():

    register_user = create_register_user()

    from domain.exceptions.invalid_password import InvalidPasswordError

    with pytest.raises(InvalidPasswordError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Yuri",
            email="yuri@email.com",
            password="A1!",
        )


def test_register_user_raises_when_password_has_no_letter():

    register_user = create_register_user()

    from domain.exceptions.invalid_password import InvalidPasswordError

    with pytest.raises(InvalidPasswordError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Yuri",
            email="yuri@email.com",
            password="12345678!",
        )


def test_register_user_raises_when_password_has_no_number():

    register_user = create_register_user()

    from domain.exceptions.invalid_password import InvalidPasswordError

    with pytest.raises(InvalidPasswordError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Yuri",
            email="yuri@email.com",
            password="Senhaaaaa!",
        )


def test_register_user_raises_when_password_has_no_uppercase():

    register_user = create_register_user()

    from domain.exceptions.invalid_password import InvalidPasswordError

    with pytest.raises(InvalidPasswordError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Yuri",
            email="yuri@email.com",
            password="senha123!",
        )


def test_register_user_raises_when_password_has_no_lowercase():

    register_user = create_register_user()

    from domain.exceptions.invalid_password import InvalidPasswordError

    with pytest.raises(InvalidPasswordError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Yuri",
            email="yuri@email.com",
            password="SENHA123!",
        )


def test_register_user_raises_when_password_has_no_special_character():

    register_user = create_register_user()

    from domain.exceptions.invalid_password import InvalidPasswordError

    with pytest.raises(InvalidPasswordError):
        register_user.execute(
            username="Yuri_dev",
            display_name="Yuri",
            email="yuri@email.com",
            password="Senha1234",
        )


def test_register_user_saves_user_in_repository():

    repository = InMemoryUserRepository()

    register_user = RegisterUser(
        username_validator=UsernameValidator,
        email_validator=EmailValidator,
        password_validator=PasswordValidator,
        password_hasher=Argon2PasswordHasher(),
        user_repository=repository,
    )

    user = register_user.execute(
        username="Yuri_dev",
        display_name="Yuri",
        email="yuri@email.com",
        password="Senha123!",
    )

    found_user = repository.find_by_username("Yuri_dev")

    assert found_user is not None
    assert found_user.id == user.id


def test_register_user_hashes_password():

    register_user = create_register_user()

    user = register_user.execute(
        username="Yuri_dev",
        display_name="Yuri",
        email="yuri@email.com",
        password="Senha123!",
    )

    assert user.password_hash != "Senha123!"
    assert Argon2PasswordHasher().verify(
        "Senha123!",
        user.password_hash,
    )