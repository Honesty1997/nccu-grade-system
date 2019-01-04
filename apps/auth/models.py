from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from core.models import Person, Timestamp
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, account, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not account:
            raise ValueError('Users must have an account')

        user = self.model(
            account=account,
        )
        user.set_password(password)
        user.is_superuser = False
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, account, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            account,
            password=password,
        )

        user.role_field = 4
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True

        user.save()
        return user

class User(AbstractBaseUser, Timestamp):
    STUDENT = 1
    TEACHER = 2
    EXECUTIVE = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (EXECUTIVE, 'Executive'),
        (ADMIN, 'Admin')
    )
    account = models.CharField(max_length=50, unique=True, default="123")
    role_field = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    USERNAME_FIELD = 'account'

    objects = UserManager()
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # It is important to note the field is used by django admin.
    # If the field is set to true, the user is allowed to access django admin.
    is_staff = models.BooleanField(default=False)

    # TODO(honesty1997): Implement the function.
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    # TODO(honesty1997): Implement the function.
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_student(self):
        return self.role_field == 1

    @property
    def is_teacher(self):
        return self.role_field == 2

    @property
    def is_executive(self):
        return self.role_field == 3

    @property
    def is_admin(self):
        return self.role_field == 4

    def __str__(self):
        return '[{}] {}'.format(self.role_field, self.account)
