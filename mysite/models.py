from django.db import models


class BaseModel(models.Model):
    @classmethod
    def create(cls, **kwargs):
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
    email = models.EmailField()
    registered_date = models.DateField(blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        abstract = True
