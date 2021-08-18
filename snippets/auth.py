from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()


class PhoneOrEmailModelBackend(ModelBackend):
    """Authenticates against user phone"""

    def authenticate(self, request, username=None, company_id=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            if username == 'admin':
                user = UserModel.objects.get(username=username)
            else:
                user = UserModel.objects.filter(company_id=company_id).get(Q(username=username) | Q(phone=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user