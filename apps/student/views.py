from django.shortcuts import render, reverse
from django.views.generic import DetailView

from mysite.views import ListView
from .models import Student
# Create your views here.
class StudentList(ListView):
    model = Student
    template_name = 'modules/student/student_list.html'
    context_object_name = 'student_list'
    paginate_by = 25
    base_url = 'student:list'

class StudentDetail(DetailView):
    model = Student
    template_name = 'modules/student/student_detail.html'
    context_object_name = 'student'

