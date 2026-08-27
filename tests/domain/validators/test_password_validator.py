import pytest

from domain.validators.password_validator import PasswordValidator
from domain.exceptions.invalid_password import InvalidPasswordError


def test_valid_password():

    PasswordValidator.validate("Senha123!")


def test_password_must_have_at_least_8_characters():

    with pytest.raises(InvalidPasswordError):
        PasswordValidator.validate("Sen1!")


def test_password_must_have_letter():

    with pytest.raises(InvalidPasswordError):
        PasswordValidator.validate("12345678!")


def test_password_must_have_number():

    with pytest.raises(InvalidPasswordError):
        PasswordValidator.validate("Senhaaaaa!")


def test_password_must_have_uppercase():

    with pytest.raises(InvalidPasswordError):
        PasswordValidator.validate("senha123!")


def test_password_must_have_lowercase():

    with pytest.raises(InvalidPasswordError):
        PasswordValidator.validate("SENHA123!")


def test_password_must_have_special_character():

    with pytest.raises(InvalidPasswordError):
        PasswordValidator.validate("Senha1234")