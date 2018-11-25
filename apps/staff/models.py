from django.db import models

from apps.auth.models import User
from mysite.models import Person, Timestamp


class Teacher(Person, Timestamp):
    
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
        return reverse('teacher:detail', kwargs={'pk': self.pk})

    def save(self):
        super().save(role='teacher')

    class Meta:
        ordering = ['id']
