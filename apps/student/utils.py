from .models import Student
from core.utils import DummyDataHandler

DUMMY_STUDENTS = [
    {
        'first_name': 'Philip',
        'last_name': 'Lin',
        'address': 'Somewhere',
        'phone_number': '093334432',
        'email': 'appl2143edd@gmail.com'
    },
    {
        'first_name': 'Harry',
        'last_name': 'Lin',
        'address': 'Somewhere',
        'phone_number': '093334432',
        'email': 'appl412e21dd@gmail.com'
    },
    {
        'first_name': 'Apple',
        'last_name': 'Lin',
        'address': 'Somewhere',
        'phone_number': '093334432',
        'email': 'ap3211pledd@gmail.com'
    },
    {
        'first_name': 'Dbian',
        'last_name': 'Lin',
        'address': 'Somewhere',
        'phone_number': '093334432',
        'email': 'appl55edd@gmail.com'
    },
    {
        'first_name': 'Linux',
        'last_name': 'Lin',
        'address': 'Somewhere',
        'phone_number': '093334432',
        'email': 'apple3dd@gmail.com'
    },
    {
        'first_name': 'Keniz',
        'last_name': 'Lin',
        'address': 'Somewhere',
        'phone_number': '093334432',
        'email': 'appl4edd@gmail.com'
    },
    {
        'first_name': 'Joane',
        'last_name': 'Chan',
        'address': 'Somewhere',
        'phone_number': '0934434432',
        'email': 'aae44dd@gmail.com'
    },
    {
        'first_name': 'Vivian',
        'last_name': 'Hwang',
        'address': 'Somewhere',
        'phone_number': '0938484432',
        'email': 'appasedd@gmail.com'
    },
]


class StudentDummyHandler(DummyDataHandler):
    model = Student
