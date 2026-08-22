from domain.exceptions.invalid_password import InvalidPasswordError

class PasswordValidator:

    @staticmethod
    def validate(password):

        if len(password) < 8:
            raise InvalidPasswordError(
                "A senha deve ter pelo menos 8 caracteres."
            )

        has_letter = any(c.isalpha() for c in password)
        if not has_letter:
            raise InvalidPasswordError(
                "A senha deve conter ao menos uma letra."
            )

        has_number = any(c.isdigit() for c in password)
        if not has_number:
            raise InvalidPasswordError(
                "A senha deve conter ao menos um número."
            )

        has_upper = any(c.isupper() for c in password)
        if not has_upper:
            raise InvalidPasswordError(
                "A senha deve conter letra maiúscula."
            )

        has_lower = any(c.islower() for c in password)
        if not has_lower:
            raise InvalidPasswordError(
                "A senha deve conter letra minúscula."
            )

        has_special = any(not c.isalnum() and not c.isspace() for c in password)
        if not has_special:
            raise InvalidPasswordError(
                "A senha deve conter caracteres especiais."
            )