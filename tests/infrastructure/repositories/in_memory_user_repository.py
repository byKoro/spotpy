from domain.entities.user import User

from infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository
)


user1 = User(
    "1",
    "Yuri_dev",
    "Yuri",
    "yuri@email.com",
    "hash_fake"
)

user2 = User(
    "2",
    "Carlos_dev",
    "Carlos",
    "carlos@email.com",
    "hash_fake"
)

user = User(
    "1",
    "Yuri_dev",
    "Yuri",
    "yuri@email.com",
    "hash_fake"
)
repository = InMemoryUserRepository()
repository.save(user1)
repository.save(user2)
repository.save(user)

found_user = repository.find_by_email("naoexiste@email.com")

print(found_user)