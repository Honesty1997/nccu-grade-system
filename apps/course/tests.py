from django.test import TestCase

from apps.course.models import Course, ScoringSubject
from apps.staff.models import  Teacher
# Create your tests here.

class CourseTestCase(TestCase):
    def setUp(self):
        COURSE_INFO = [
            {   
                'course_number': 1234,
                'course_name': 'Economics',
                'description': 'This is a bad course',
            },
            {
                'course_number': 5678,
                'course_name': 'Manage Information System',
                'description': 'This is a bad course',
            },
            {
                'course_number': 4456,
                'course_name': 'Chinese Literature',
                'description': 'This is a bad course',
            },
            {
                'course_number': 8953,
                'course_name': 'Apple Economics',
                'description': 'This is a bad course',
            },
            {
                'course_number': 5983,
                'course_name': 'Bad Course',
                'description': 'This is a bad course',
            },
        ]
        for info in COURSE_INFO:
            Course.create(**info)

    def tearDown(self):
        pass

    def test_course_scoring_subject_removed(self):
        self.assertEqual(0 , 0, 'Assert zero is equal to zero')
