from domain.exceptions.username_already_exists import UsernameAlreadyExistsError
from domain.exceptions.email_already_exists import EmailAlreadyExistsError
from domain.entities.user import User
from uuid import uuid4

class RegisterUser:

    def __init__(
            self, 
            username_validator, 
            email_validator, 
            password_validator,
            password_hasher,
            user_repository,
            ):
        self.username_validator = username_validator
        self.email_validator = email_validator
        self.password_validator = password_validator
        self.password_hasher = password_hasher
        self.user_repository = user_repository
        
    def execute(self, username, display_name, email, password):
        self.username_validator.validate(username)
        self.email_validator.validate(email)
        self.password_validator.validate(password)

        existing_user = self.user_repository.find_by_username(username)
        if existing_user is not None:
            raise UsernameAlreadyExistsError(
                "Username já está sendo utilizado."
            )

        existing_email = self.user_repository.find_by_email(email)
        if existing_email is not None:
            raise EmailAlreadyExistsError(
                "Email já está cadastrado."
            )

        password_hash = self.password_hasher.hash(password)

        user_id = str(uuid4())

        user = User(
            user_id,
            username,
            display_name,
            email,
            password_hash
        )

        self.user_repository.save(user)

        return user