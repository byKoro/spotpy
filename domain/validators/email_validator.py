import re

from domain.exceptions.invalid_email import InvalidEmailError

class EmailValidator:

    @staticmethod
    def validate(email):

        resultado = re.fullmatch(
            r".+@.+\..+",
            email
            )

        if resultado is None:
            raise InvalidEmailError(
                "Email é inválido."
                )