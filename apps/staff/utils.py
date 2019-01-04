from .models import Teacher
from core.utils import DummyDataHandler
DUMMY_TEACHERS = [
        {
            'first_name': 'Han',
            'last_name': 'haha',
            'phone_number': '123452',
            'email': 'bbb@gmail.com',
        },
        {
            'first_name': 'SSS',
            'last_name': 'haha',
            'phone_number': '123452',
            'email': 'ccc@gmail.com',
        },
        {
            'first_name': 'GGG',
            'last_name': 'haha',
            'phone_number': '123452',
            'email': 'asd@gmail.com',
        },
        {
            'first_name': 'EEEE',
            'last_name': 'haha',
            'phone_number': '123452',
            'email': 'bbsdf@gmail.com',
        },
        {
            'first_name': 'HEEWan',
            'last_name': 'haha',
            'phone_number': '123452',
            'email': 'didddid@gmail.com',
        },
    ]

class TeacherDummyHandler(DummyDataHandler):
    model = Teacher
