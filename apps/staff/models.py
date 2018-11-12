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

    def save(self):
        self.teacher_number = Teacher.create_teacher_number()
        super().save(role='professor')

    @staticmethod
    def create_teacher_number():
        t_num_list = [i for i in range(200000000, 209999999)]
        for num in t_num_list:
            if not Teacher.objects.filter(teacher_number=num):
                return num

