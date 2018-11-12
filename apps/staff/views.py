from django.shortcuts import render, reverse
from django.views.generic import DetailView, CreateView, UpdateView

from apps.auth.models import User 
from mysite.views import ListView
from .models import Teacher
# Create your views here.
class TeacherList(ListView):
    model = Teacher
    template_name = 'modules/teacher/teacher_list.html'
    context_object_name = 'teacher_list'
    paginate_by = 25
    base_url = 'teacher:list'

class TeacherDetail(DetailView):
    model = Teacher
    template_name = 'modules/teacher/teacher_detail.html'
    context_object_name = 'teacher'


class TeacherCreate(CreateView):
    model = Teacher
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'phone_number']

class TeacherUpdate(UpdateView):
    model = Teacher
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'year_in_school']