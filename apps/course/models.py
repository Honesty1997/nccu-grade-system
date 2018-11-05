from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from mysite.models import BaseModel, Timestamp
from apps.student.models import Student
from apps.auth.models import User
# Create your models here.
class Course(BaseModel, Timestamp):
    course_number = models.PositiveIntegerField(blank=True, null=True)
    course_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    registered_students = models.ManyToManyField(Student)

    def __str__(self):
        return self.course_name

    def course_average(self):
        pass

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

    def add_new_subject(self, title: str):
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
        obj, created = ScoringSubject.objects.get_or_create(title=title, course=self)
        if created:
            from apps.grade.models import Grade
            for student in obj.course.registered_students.all():
                set_default_grade = Grade(
                    student=student, subject=obj, score=0)
                set_default_grade.save()
        return obj, created
    # TODO(3): Please implement this function. The function should take the title of a ScoringSubject,  
    # and remove corresponding object in the database. Return the removed object as return value.
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
        return None

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('course:detail', kwargs={'pk': self.pk})

    # TODO Please implement this function. Just make sure the number is unique and meaningful.
    @staticmethod
    def create_course_number(self, course_list):
        if self.course_number not in course_list:
            return self.course_number

    def save(self):
        self.course_number = Student.create_student_number()
        super().save()

class ScoringSubject(BaseModel, Timestamp):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

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
