from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.auth.models import User 
from mysite.views import ListView
from .models import Student
# Create your views here.
class StudentList(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'modules/student/student_list.html'
    context_object_name = 'student_list'
    paginate_by = 25
    base_url = 'student:list'

class StudentDetail(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'modules/student/student_detail.html'
    context_object_name = 'student'


class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'phone_number', 'year_in_school']

class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'year_in_school']