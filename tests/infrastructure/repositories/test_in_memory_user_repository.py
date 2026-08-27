from domain.entities.user import User
from infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository
)


def create_user(
    user_id="1",
    username="Yuri_dev",
    display_name="Yuri",
    email="yuri@email.com",
    password_hash="hash_fake",
):
    return User(
        user_id,
        username,
        display_name,
        email,
        password_hash,
    )


def test_save_user():

    repository = InMemoryUserRepository()

    user = create_user()

    repository.save(user)

    assert repository.users == [user]


def test_find_by_username_returns_user():

    repository = InMemoryUserRepository()

    user = create_user()

    repository.save(user)

    found_user = repository.find_by_username("Yuri_dev")

    assert found_user == user


def test_find_by_username_returns_none_when_user_does_not_exist():

    repository = InMemoryUserRepository()

    user = create_user()

    repository.save(user)

    found_user = repository.find_by_username("Carlos_dev")

    assert found_user is None


def test_find_by_email_returns_user():

    repository = InMemoryUserRepository()

    user = create_user()

    repository.save(user)

    found_user = repository.find_by_email("yuri@email.com")

    assert found_user == user


def test_find_by_email_returns_none_when_user_does_not_exist():

    repository = InMemoryUserRepository()

    user = create_user()

    repository.save(user)

    found_user = repository.find_by_email(
        "naoexiste@email.com"
    )

    assert found_user is None