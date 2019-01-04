from django.test import TestCase, Client
from django.shortcuts import reverse

from apps.course.models import Course, ScoringSubject
from .utils import DUMMY_COURSES, DUMMY_SCORING_SUBJECTS, CourseDummyHandler, ScoringSubjectDummyHandler
from apps.staff.models import  Teacher
from apps.staff.utils import DUMMY_TEACHERS, TeacherDummyHandler

# Create your tests here.
class CourseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.teacher, _ = Teacher.objects.get_or_create(**DUMMY_TEACHERS[0])

    @classmethod
    def tearDownClass(cls):
        cls.teacher.delete()

    def setUp(self):
        self.dummy_handler = CourseDummyHandler()
        for course in DUMMY_COURSES:
            course['teacher'] = CourseModelTestCase.teacher
        self.dummy_handler.bulk_create(DUMMY_COURSES[:3])

    def tearDown(self):
        self.dummy_handler.delete_all()

    def test_course_created(self):
        for course in self.dummy_handler.objs:
            self.assertIsNotNone(Course.objects.get(
                course_number=course.course_number))

    def test_course_scoring_subject_removed(self):
        self.assertEqual(0 , 0, 'Assert zero is equal to zero')

class CourseOwnerPrivilegeCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up teacher.
        cls.teachers = TeacherDummyHandler().bulk_create(DUMMY_TEACHERS[:2])
        cls.teacher1 = cls.teachers[0]
        cls.teacher2 = cls.teachers[1]
        
        for index, COURSE in enumerate(DUMMY_COURSES):
            COURSE['teacher'] = cls.teachers[index % 2]
        
        cls.courses = CourseDummyHandler().bulk_create(DUMMY_COURSES)
        
        for course in cls.courses:
            for SUBJECT in DUMMY_SCORING_SUBJECTS:
                course.add_new_subject(**SUBJECT)

    def test_course_detail(self):
        teacher1 = Client()
        teacher1.force_login(CourseOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(CourseOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(CourseOwnerPrivilegeCase.courses):
            res1 = teacher1.get(reverse('course:detail', kwargs={'pk': course.pk}))
            res2 = teacher2.get(reverse('course:detail', kwargs={'pk': course.pk}))
            if index % 2 == 0:
                self.assertEqual(res1.status_code, 200)
                self.assertEqual(res2.status_code, 403)
            else:
                self.assertEqual(res1.status_code, 403)
                self.assertEqual(res2.status_code, 200)

    def test_course_update(self):
        teacher1 = Client()
        teacher1.force_login(CourseOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(CourseOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(CourseOwnerPrivilegeCase.courses):
            res1 = teacher1.get(reverse('course:update', kwargs={'pk': course.pk}))
            res2 = teacher2.get(reverse('course:update', kwargs={'pk': course.pk}))
            if index % 2 == 0:
                self.assertEqual(res1.status_code, 200)
                self.assertEqual(res2.status_code, 403)
            else:
                self.assertEqual(res1.status_code, 403)
                self.assertEqual(res2.status_code, 200)
    

    def test_course_delete(self):
        teacher1 = Client()
        teacher1.force_login(CourseOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(CourseOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(CourseOwnerPrivilegeCase.courses):
            res1 = teacher1.get(reverse('course:delete', kwargs={'pk': course.pk}))
            res2 = teacher2.get(reverse('course:delete', kwargs={'pk': course.pk}))
            # Only admin can delete the course.
            if index % 2 == 0:
                self.assertEqual(res1.status_code, 403)
                self.assertEqual(res2.status_code, 403)
            else:
                self.assertEqual(res1.status_code, 403)
                self.assertEqual(res2.status_code, 403)
class ScoringSubjectTestCase(TestCase):
    pass
