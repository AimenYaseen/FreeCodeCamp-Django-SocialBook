from django.core.exceptions import ValidationError

from user_auth.db_actions import UserDbActions
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserAuthValidators:
    @staticmethod
    def validate_username(value):
        try:
            UnicodeUsernameValidator(value)
        except ValidationError as exc:
            raise ValidationError(exc)

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise ValidationError(exc)

    @staticmethod
    def validate_signup_input(data):
        email = data.get('email').strip()
        username = data.get('username').strip()
        password = data.get('password').strip()

        # validate username and email
        UserDbActions.check_user('username', username=username)
        UserDbActions.check_user('email', email=email)

        # validate username and password
        UserAuthValidators.validate_username(username)
        UserAuthValidators.validate_password(password)

        return {
            'email': email,
            'password': password,
            'username': username,
        }
