from django.db import models
from core.models import Person


class Teacher(Person):
    def save(self):
        super().save(role='teacher')
