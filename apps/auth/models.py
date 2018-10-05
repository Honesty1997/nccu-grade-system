from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from mysite.models import Person, Timestamp
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )

        user.role_field = 4
        user.save()
        return user

class User(AbstractBaseUser, Person, Timestamp):
    STUDENT = 1
    PROFESSOR = 2
    STAFF = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (PROFESSOR, 'Professor'),
        (STAFF, 'Staff'),
        (ADMIN, 'Admin')
    )

    role_field = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    USERNAME_FIELD = 'email'

    objects = UserManager()
    is_active = models.BooleanField(default=True)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_student(self):
        return self.role_field == 1

    @property
    def is_professor(self):
        return self.role_field == 2

    @property
    def is_staff(self):
        return self.role_field == 3

    @property
    def is_admin(self):
        return self.role_field == 4

    def __str__(self):
        return '[{}] {}'.format(self.role, self.name)
