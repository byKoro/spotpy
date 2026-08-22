from abc import ABC, abstractmethod

class PasswordHasher(ABC):

    @abstractmethod
    def hash(self, password):
        pass

    @abstractmethod
    def verify(self, password, password_hash):
        pass