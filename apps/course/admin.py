from django.contrib import admin

from .models import Course, ScoringSubject

# Register your models here.
admin.site.register(Course)
admin.site.register(ScoringSubject)
