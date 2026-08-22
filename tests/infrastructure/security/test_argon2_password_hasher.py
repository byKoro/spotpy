from infrastructure.security.argon2_password_hasher import (
    Argon2PasswordHasher
)


hasher = Argon2PasswordHasher()

password = "Senha123!"

password_hash = hasher.hash(password)

print(hasher.verify(password, password_hash))
print(hasher.verify("SenhaErrada123!", password_hash))