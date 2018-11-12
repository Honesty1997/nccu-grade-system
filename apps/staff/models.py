from django.db import models
from apps.auth.models import User
from mysite.models import Person, Timestamp
# TODO(4): Add a Teacher model here. I already implement a 
# parent class called Person at 'mysite/models'. Plz import 
# that class as base class. Add any attribute you want if 
# you see the attribute is necessary for this project.

class Professor(Person, Timestamp):
    professor_number = models.PositiveIntegerField(blank=True, null=True)
    
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
        return reverse('professor:detail', kwargs={'pk': self.pk})

    def save(self):
        self.professor_number = Professor.create_professor_number()
        super().save(role='professor')

    # TODO Please implement this function. Just make sure the number is unique and meaningful.
    @staticmethod
    def create_professor_number():
        return 2

    #資料顯示順序按id number
    class Meta:
        ordering = ['id']
