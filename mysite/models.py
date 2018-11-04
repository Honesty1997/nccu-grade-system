from django.db import models

class BaseModel(models.Model):
    @classmethod
    def create(cls, **kwargs):
        """
            A quick way to use get_or_create on Class level.
        """
        obj, created = cls.objects.get_or_create(**kwargs)
        return obj, created

    def info(self, **kwargs):
        info = {}
        for key, value in kwargs.items():
            info[key] = value
        return info

    class Meta:
        abstract = True

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Person(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    cellphone_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    registered_date = models.DateField(blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)
    user = models.OneToOneField('site_auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def save(self, **kwargs):
        from apps.auth.models import User
        role_field_maping = {
            'student': 1,
            'professor': 2,
            'executive': 3,
            'admin': 4,
            'teacher': 5,
        }
        role = kwargs.get('role')
        if self.pk is None:
            if role != 4:
                user = User.objects.create_user(account=self.email, password=self.phone_number)
                user.role_field = role_field_maping[role]
            else:
                user = User.objects.create_superuser(
                    self.email, self.phone_number)
        super().save()

    class Meta:
        abstract = True
