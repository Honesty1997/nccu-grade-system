from django.db import models
from mysite.models import Person, Timestamp
# TODO(4): Add a Teacher model here. I already implement a 
# parent class called Person at 'mysite/models'. Plz import 
# that class as base class. Add any attribute you want if 
# you see the attribute is necessary for this project.

class Teacher(Person, Timestamp):
    pass