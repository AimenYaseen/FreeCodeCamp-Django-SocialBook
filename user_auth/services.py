from django.contrib import messages

from user_auth.db_actions import UserDbActions
from user_auth.validators import UserAuthValidators


class UserAuthServices:
    @staticmethod
    def signup_service(request):
        validated_data = UserAuthValidators.validate_signup_input(request.POST)
        UserDbActions.create_user(validated_data)
        messages.info(request, 'User has created Successfully!')
