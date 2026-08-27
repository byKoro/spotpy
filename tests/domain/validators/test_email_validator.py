import pytest

from domain.validators.email_validator import EmailValidator
from domain.exceptions.invalid_email import InvalidEmailError


def test_valid_email():

    EmailValidator.validate("yuri@email.com")


def test_valid_email_with_subdomain():

    EmailValidator.validate("yuri@mail.email.com")


def test_invalid_email_without_at():

    with pytest.raises(InvalidEmailError):
        EmailValidator.validate("yuriemail.com")


def test_invalid_email_without_domain():

    with pytest.raises(InvalidEmailError):
        EmailValidator.validate("yuri@")


def test_invalid_email_without_extension():

    with pytest.raises(InvalidEmailError):
        EmailValidator.validate("yuri@email")