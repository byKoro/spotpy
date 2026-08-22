class User:
    def __init__(self, id, username, display_name, email, password_hash):
        self._id = id
        self._username = username
        self._display_name = display_name
        self._email = email
        self._password_hash = password_hash

    def change_display_name(self, new_display_name):
        self._display_name = new_display_name

    @property
    def display_name(self):
        return self._display_name

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def password_hash(self):
        return self._password_hash


