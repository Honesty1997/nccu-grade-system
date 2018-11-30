from django.db import models
from uuid import uuid4
from apps.auth.models import User
from mysite.models import Person, Timestamp

# Create your models here.
class Student(Person, Timestamp):
    student_number = models.CharField(unique=True, blank=True, null=True, max_length=32)

    def info(self, **kwargs):
        info = super().info(**kwargs)
        info['pk'] = self.pk
        info['first_name'] = self.first_name
        info['last_name'] = self.last_name
        info['address'] = self.address
        info['cellphone_number'] = self.cellphone_number
        info['email'] = self.email
        info['name'] = self.name
        return info

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('student:detail', kwargs={'pk': self.pk})

    def save(self):
        self.student_number = Student.create_student_number()
        super().save(role='student')

    @staticmethod
    def create_student_number():
        return uuid4().hex

    class Meta:
        ordering = ['id']
