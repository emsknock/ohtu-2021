import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if not re.match(r"^[a-zA-Z]{3,}$", username):
            raise UserInputError("Username must only contain letters a-z and be at least 3 characters long")
        if (not re.match(r"^[a-zA-Z0-9]{8,}$", password)) or (not re.search(r"\d", password)):
            raise UserInputError("Password must be at least 8 characters long and contain at least 1 number")