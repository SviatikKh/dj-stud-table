from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    pass


class CustomUser(AbstractBaseUser):
    pass
