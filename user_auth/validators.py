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
            raise ValidationError(str(exc))

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise ValidationError(str(exc))
