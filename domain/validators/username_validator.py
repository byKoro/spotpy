import re

from domain.exceptions.invalid_username import InvalidUsernameError


class UsernameValidator:

    @staticmethod
    def validate(username):

        resultado = re.fullmatch(
            r"[a-zA-Z0-9_-]+",
            username
        )

        if resultado is None:
            raise InvalidUsernameError(
                "Username contém caracteres inválidos!"
            )

        if len(username) > 20:
            raise InvalidUsernameError(
                "Username não pode ter mais de 20 caracteres!"
            )