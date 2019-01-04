from core.utils import DummyDataHandler

from .models import ScoringSubject, Course

DUMMY_COURSES = [
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

DUMMY_SCORING_SUBJECTS = [
    {
        'title': 'homework1',
        'subject_type': 'Q',
    },
    {
        'title': 'quiz1',
        'subject_type': 'H'
    }
]

class CourseDummyHandler(DummyDataHandler):
    model = Course

class ScoringSubjectDummyHandler(DummyDataHandler):
    model = ScoringSubject
