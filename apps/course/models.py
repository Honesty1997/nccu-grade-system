from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from uuid import uuid4
from core.models import BaseModel, Timestamp
from apps.student.models import Student
from apps.staff.models import Teacher
from apps.auth.models import User
# Create your models here.
class Course(BaseModel, Timestamp):
    course_number = models.CharField(unique=True, blank=True, null=True, max_length=32)
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    registered_students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.course_name

    def register(self, students):
        """
            Args:
                Students List[Student]: list of student object that need to be registered to 
                the course.
            Returns:
                A integer indicates how many students are successfully registered to the course.
        """
        from apps.grade.models import Grade
        count = 0
        all_scoring_subjects = self.scoringsubject_set.all()
        for student in students:
            # If the student haven't registered to the course, add the student to the course.
            if student not in self.registered_students.all():
                count += 1
                self.registered_students.add(student)
                # If the Course have some default scoringsubject, set the subject score to 0
                # as default.
                for subject in all_scoring_subjects:
                    set_default_score = Grade(subject=subject, student=student, score=0)
                    set_default_score.save()
        self.save()
        return self, count

    def unregister(self, students):
        from apps.grade.models import Grade
        count = 0
        all_scoring_subjects = self.scoringsubject_set.all()
        for student in students:
            # If the student have registered to the course, remove the student from the course.
            if student in self.registered_students.all():
                count += 1
                self.registered_students.remove(student)
                # Remove the student's scoring_subjects at the same time.
                for subject in all_scoring_subjects:
                    student_grade = Grade.objects.get(student=student, subject=subject)
                    student_grade.delete()
        self.save()
        return self, count

    def add_new_subject(self, title: str, subject_type: str):
        """Add new subject to a Course.

            Args:
                title str: The title of the new subject.
            Returns:
                ScoringSubject: The subject which is created.
                created: Whether the subject is newly created.
            Raises:
                TypeError: When the argument is not string.
        """
        if not isinstance(title, str):
            raise TypeError('Title should be string.')
        obj, created = ScoringSubject.objects.get_or_create(title=title, course=self, subject_type=subject_type)
        if created:
            from apps.grade.models import Grade
            for student in obj.course.registered_students.all():
                set_default_grade = Grade(
                    student=student, subject=obj, score=0)
                set_default_grade.save()
        return obj, created

    def remove_existing_subject(self, title):
        """Remove a existing subject from a course.

            Args:
                title str: The title of the removed subject.
            Returns:
                The removed subject.
            Raise:
                TypeError: The argument is not str.
                ObjectDoesNotExist: When the title object is not found.

        """
        if not isinstance(title, str):
            raise TypeError('Title should be string.')
        removed_subject = self.scoringsubject_set.get(title=title)
        removed_subject.delete()
        return removed_subject

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('course:detail', kwargs={'pk': self.pk})

    @staticmethod
    def create_course_number():
        # TODO: Currently use uuid for convenience. Should use more proper way to 
        # represent course number.
        return uuid4()

    def get_total_score(self, student=None):
        scoringsubject_list = []
        for subject in self.scoringsubject_set.all():
            subject_info = subject.info()
            if student:
                subject_info['current_score'] = subject.get_student_score(student)
            scoringsubject_list.append(subject_info)
        return scoringsubject_list

    def save(self, **kwargs):
        if self.course_number is None:
            self.course_number = Course.create_course_number()
        super().save(**kwargs)

class ScoringSubject(BaseModel, Timestamp):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    SUBJECT_TYPE = (
        ('Q', '小考'),
        ('H', '作業'),
    )
    subject_type = models.CharField(max_length=2, null=True, choices=SUBJECT_TYPE)

    @property
    def average(self):
        total = 0
        count = 0
        for subject in self.grade_set.all():
            total += subject.score
            count += 1

        try:
            average = total / count
        except ZeroDivisionError:
            average = 0
        return average

    def __str__(self):
        return '[{}]{}'.format(self.course, self.title)

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('course:subject', kwargs={'pk': self.pk })

    def get_score_list(self):
        grades = self.grade_set.all()
        scores_list = [grade.score for grade in grades]
        return scores_list
    
    def get_student_score(self, student):
        grade = self.grade_set.get(student=student)
        return grade.score

    def info(self):
        subject_type = '作業' if self.subject_type == 'H' else '小考'
        subject_info = {
            'title': self.title,
            'subject_type': subject_type,
            'score_list': self.get_score_list()
        }
        return subject_info
