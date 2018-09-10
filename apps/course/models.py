from django.db import models

from mysite.models import BaseModel, Timestamp
from apps.student.models import Student

# Create your models here.
class Course(BaseModel, Timestamp):
    course_number = models.CharField(
        max_length=40,
        db_index=True, 
        unique=True
    )
    course_name = models.CharField(max_length=50)
    # teacher = models.ForeignKey()
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
        pass

    def search_student_score(self, student):
        pass

    def add_new_subject(self, title):
        """
            Args:
                title String: The title of the new subject.
            Returns:
                The ScoringSubject created.
        """
        obj, created = ScoringSubject.objects.get_or_create(title=title, course=self)
        if created:
            from apps.grade.models import Grade
            for student in obj.course.registered_students.all():
                set_default_grade = Grade(
                    student=student, subject=obj, score=0)
                set_default_grade.save()
        return obj

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('course_detail', kwargs={'pk': self.pk})

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


