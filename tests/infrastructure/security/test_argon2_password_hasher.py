from infrastructure.security.argon2_password_hasher import (
    Argon2PasswordHasher
)


def test_hash_password():

    hasher = Argon2PasswordHasher()

    password = "Senha123!"

    password_hash = hasher.hash(password)

    assert password_hash != password


def test_verify_correct_password():

    hasher = Argon2PasswordHasher()

    password = "Senha123!"

    password_hash = hasher.hash(password)

    assert hasher.verify(password, password_hash)


def test_verify_incorrect_password():

    hasher = Argon2PasswordHasher()

    password = "Senha123!"

    password_hash = hasher.hash(password)

    assert not hasher.verify(
        "SenhaErrada123!",
        password_hash,
    )


def test_same_password_generates_different_hashes():

    hasher = Argon2PasswordHasher()

    password = "Senha123!"

    hash1 = hasher.hash(password)
    hash2 = hasher.hash(password)

    assert hash1 != hash2