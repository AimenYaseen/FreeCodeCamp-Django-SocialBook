from django.contrib.auth.models import User
from django.core.exceptions import BadRequest

from users.models import Profile


class UserDbActions:
    @staticmethod
    def check_user(field, **kwargs):
        """
        check if user exists with the given keyword arguments
        raise an error if it does not exist
        """
        if User.objects.filter(**kwargs).exists():
            raise BadRequest(f'User with this {field} "{kwargs.get(field)}" already Exists')

    @staticmethod
    def create_user(data):
        """
        create user instance with the following data
        """
        user = User.objects.create_user(**data)
        Profile.objects.create(user=user, token=user.id)
