import datetime

from django.db import models

from apps.auth.models import User
from mysite.models import Person, Timestamp

# Create your models here.
class Student(Person, Timestamp):
    fi = 1
    soi = 1
    ji = 1
    sei = 1

    student_number = models.PositiveIntegerField(blank=True, null=True)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

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

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('student:detail', kwargs={'pk': self.pk})

    def save(self):
        self.student_number = Student.create_student_number()
        super().save(role='student')

    # TODO Please implement this function. Just make sure the number is unique and meaningful.
    @staticmethod
    def create_student_number(year_in_school):
       
        now = datetime.datetime.now()
        year = now.year
        if year_in_school == 'FR':
            head = year
            head = str(head)
            number = head + "{0:0>3}".format(Student.fi)
            Student.fi += 1
            number = int(number)
        elif year_in_school == "SO":
            head = year - 1
            head = str(head)
            number = head + "{0:0>3}".format(Student.soi)
            Student.soi += 1
            number = int(number)
        elif year_in_school == 'JU':
            head = year - 2
            head = str(head)
            number = head + "{0:0>3}".format(Student.ji)
            Student.ji += 1
            number = int(number)
        elif year_in_school == 'SE':
            head = year - 3
            head = str(head)
            number = head + "{0:0>3}".format(Student.sei)
            Student.sei += 1
            number = int(number)
        return number

    
    def save(self):
        self.student_number = Student.create_student_number(self.year_in_school)
        super().save(role='student')
    class Meta:
        ordering = ['id']
