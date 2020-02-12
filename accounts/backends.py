from django.contrib.auth.models import User


class EmailAuth:
    """ Authenticate a user by exact match on the email and password """
    def authenticate(self, username=None, password=None):
        """ get an instance of 'User' based off of the email and verify the password """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                # if validation is good return user
                return user
            return None
            # if user does not exist, return home
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ used by django auth systems to retreive a user instance """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
