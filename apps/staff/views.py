from django.shortcuts import render, reverse
from django.views.generic import DetailView, CreateView, UpdateView

from apps.auth.models import User 
from mysite.views import ListView
from .models import Teacher

# Create your views here.
class TeacherList(ListView):
    model = Teacher
    template_name = 'modules/staff/teacher_list.html'
    context_object_name = 'teacher_list'
    paginate_by = 25
    base_url = 'staff:list'

class TeacherDetail(DetailView):
    model = Teacher
    template_name = 'modules/staff/teacher_detail.html'
    context_object_name = 'teacher'


# class StudentCreate(CreateView):
#     model = Student
#     template_name = 'modules/common/form.html'
#     context_object_name = 'form'
#     fields = ['first_name', 'last_name', 'address',
#               'email', 'cellphone_number', 'phone_number', 'year_in_school']

# class StudentUpdate(UpdateView):
#     model = Student
#     template_name = 'modules/common/form.html'
#     context_object_name = 'form'
#     fields = ['first_name', 'last_name', 'address',
#               'email', 'cellphone_number', 'year_in_school']


