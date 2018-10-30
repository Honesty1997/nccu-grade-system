from django.db import models

from apps.auth.models import User
from mysite.models import Person, Timestamp

# Create your models here.
class Student(Person, Timestamp):
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
    def create_student_number():
        return 1

    class Meta:
        ordering = ['id']
