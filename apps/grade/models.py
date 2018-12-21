from django.db import models

from core.models import BaseModel, Timestamp
from apps.student.models import Student
from apps.course.models import Course, ScoringSubject
from .errors import ScoreOutOfRangeError

# Create your models here.
class Grade(BaseModel, Timestamp):
    subject = models.ForeignKey(
        ScoringSubject,
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE
    )
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def save(self, **kwargs):
        score = kwargs.get('score', 0)

        # check if score out of range
        if score > 100 or score < 0:
            raise ScoreOutOfRangeError()

        super().save(**kwargs)
    
    def __str__(self):
        return '[{}]{} - {} / {}'.format(self.subject.course, self.subject.title, self.student, self.score)
