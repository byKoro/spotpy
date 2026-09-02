from domain.exceptions.invalid_password import InvalidPasswordError


class LoginUser:

    def __init__(self, user_repository, password_hasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, username, password):
        user = self.user_repository.find_by_username(username)

        if user is None:
            raise InvalidPasswordError("Usuário ou senha inválidos.")

        if not self.password_hasher.verify(password, user.password_hash):
            raise InvalidPasswordError("Usuário ou senha inválidos.")

        return user
