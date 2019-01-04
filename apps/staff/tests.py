from django.test import TestCase
from .utils import TeacherDummyHandler, DUMMY_TEACHERS
from .models import Teacher
# Create your tests here.

class TeacherTestCase(TestCase):
    def setUp(self):
        self.dummy_handler = TeacherDummyHandler()
        self.dummy_handler.bulk_create(DUMMY_TEACHERS[:3])

    def tearDown(self):
        self.dummy_handler.delete_all()

    def test_teacher_created(self):
        for teacher in self.dummy_handler.objs:
            self.assertIsNotNone(Teacher.objects.get(pk=teacher.pk))
    
    def test_teacher_associated_user_created(self):
        for teacher in self.dummy_handler.objs:
            self.assertTrue(hasattr(teacher, 'user'))
    
    def test_teacher_associated_user_is_teacher(self):
        for teacher in self.dummy_handler.objs:
            self.assertTrue(teacher.user.is_teacher)

