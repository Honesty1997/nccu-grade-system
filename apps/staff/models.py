from mysite.models import Person
from django.db import models
from mysite.models import Person


class Teacher(Person):
    teacher_number = models.PositiveIntegerField(blank=True, null=True, unique=True)
    office = models.CharField(max_length=50, blank=True)
    belong_department = models.CharField(max_length=50, blank=True)
    is_chairman =  models.BooleanField(default=False, blank=True)
    year_in_school = models.CharField(max_length=2, blank=True)

    def info(self, **kwargs):
        info = super().info(**kwargs)
        info['pk'] = self.pk
        info['first_name'] = self.first_name
        info['last_name'] = self.last_name
        info['address'] = self.address
        info['cellphone_number'] = self.cellphone_number
        info['email'] = self.email
        info['year_in_school'] = self.year_in_school
        info['name'] = self.name
        return info

    def save(self):
        teacher = super().save(role='teacher')
    
