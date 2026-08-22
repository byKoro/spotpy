from application.use_cases.register_user import RegisterUser
from domain.validators.username_validator import UsernameValidator
from domain.validators.email_validator import EmailValidator
from domain.validators.password_validator import PasswordValidator
from infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository
)
from infrastructure.security.argon2_password_hasher import (
    Argon2PasswordHasher
)


repository = InMemoryUserRepository()

register_user = RegisterUser(
    UsernameValidator,
    EmailValidator,
    PasswordValidator,
    Argon2PasswordHasher(),
    repository
)

user = register_user.execute(
    "Yuri_dev",
    "Yuri",
    "yuri@email.com",
    "Senha123!"
)

print(user.id)
print(user.username)
print(user.display_name)
print(user.email)
print(user.password_hash)

hasher = Argon2PasswordHasher()

print(hasher.verify(
    "SenhaErrada123!",
    user.password_hash
))