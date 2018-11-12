from django.db import models

from apps.auth.models import User
from mysite.models import Person, Timestamp

# TODO(4): Add a Teacher model here. I already implement a 
# parent class called Person at 'mysite/models'. Plz import 
# that class as base class. Add any attribute you want if 
# you see the attribute is necessary for this project.

class Teacher(Person, Timestamp):
    teacher_number = models.PositiveIntegerField(blank=True, null=True)

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
        self.teacher_number = Teacher.create_teacher_number()
        super().save(role='professor')

    # TODO Please implement this function. Just make sure the number is unique and meaningful.
    @staticmethod
    def create_teacher_number():
        last_teacher = Teacher.objects.all().reverse()[0]
        th_num = last_teacher.teacher_number + 1
        return th_num
    
    class Meta:
        ordering = ['id']