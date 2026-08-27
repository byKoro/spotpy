import pytest

from domain.validators.username_validator import UsernameValidator
from domain.exceptions.invalid_username import InvalidUsernameError


def test_valid_username():

    UsernameValidator.validate("Yuri_dev")


def test_username_accepts_hyphen():

    UsernameValidator.validate("Yuri-dev")


def test_username_accepts_numbers():

    UsernameValidator.validate("Yuri123")


def test_username_rejects_special_characters():

    with pytest.raises(InvalidUsernameError):
        UsernameValidator.validate("Yuri@dev")


def test_username_rejects_spaces():

    with pytest.raises(InvalidUsernameError):
        UsernameValidator.validate("Yuri dev")


def test_username_rejects_more_than_20_characters():

    with pytest.raises(InvalidUsernameError):
        UsernameValidator.validate("a" * 21)