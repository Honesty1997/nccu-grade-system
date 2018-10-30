from django.shortcuts import render, reverse
from django.views.generic import DetailView, CreateView, UpdateView

from apps.auth.models import User 
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


class StudentCreate(CreateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'phone_number', 'year_in_school']

class StudentUpdate(UpdateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'year_in_school']
