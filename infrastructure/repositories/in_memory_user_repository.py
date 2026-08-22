from domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.users = []

    def find_by_username(self, username):
        for user in self.users:
            if username == user.username:
                return user
            
        return None

    def find_by_email(self, email):
        for user in self.users:
            if email == user.email:
                return user

        return None


    def save(self, user):
        self.users.append(user)

