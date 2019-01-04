from django.test import TestCase
from apps.auth.models import User

from .utils import StudentDummyHandler, DUMMY_STUDENTS
from .models import Student
# Create your tests here.


class StudentTestCase(TestCase):
    def setUp(self):
        self.dummy_handler = StudentDummyHandler()
        self.dummy_handler.bulk_create(DUMMY_STUDENTS[:3])

    def tearDown(self):
        self.dummy_handler.delete_all()

    def test_student_created(self):
        for student in self.dummy_handler.objs:
            self.assertIsNotNone(Student.objects.get(pk=student.pk))

    def test_student_associated_user_created(self):
        for student in self.dummy_handler.objs:
            self.assertTrue(hasattr(student, 'user'))

    def test_student_associated_user_is_student(self):
        for student in self.dummy_handler.objs:
            self.assertTrue(student.user.is_student)
