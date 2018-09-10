from django.shortcuts import render, reverse
from django.views.generic import DetailView

from mysite.views import ListView
from .models import Course, ScoringSubject
# Create your views here.

class ListCourse(ListView):
    model = Course
    template_name = 'modules/course/course.html'
    context_object_name = 'course_list'
    base_url = 'course:list'
    paginate_by = 25

class DetailCourse(DetailView):
    model = Course
    template_name = 'modules/course/course_detail.html'
    contex_object_name = 'course'

class DetailSubject(DetailView):
    model = ScoringSubject
    template_name = 'modules/course/subject.html'
    context_object_name = 'subject'
