from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def find_by_username(self, username):
        pass

    @abstractmethod
    def find_by_email(self, email):
        pass

    @abstractmethod
    def save(self, user):
        pass

