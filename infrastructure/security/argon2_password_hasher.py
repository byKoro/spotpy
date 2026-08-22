from argon2 import PasswordHasher

from argon2.exceptions import VerifyMismatchError

from domain.services.password_hasher import (
    PasswordHasher as PasswordHasherContract
)


class Argon2PasswordHasher(PasswordHasherContract):

    def __init__(self):
        self._hasher = PasswordHasher()

    def hash(self, password):
        return self._hasher.hash(password)

    def verify(self, password, password_hash):
        try:
            return self._hasher.verify(password_hash, password)
        except VerifyMismatchError:
            return False