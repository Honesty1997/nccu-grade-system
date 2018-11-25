from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, View

from apps.auth.models import User 
from mysite.views import ListView
from .models import Teacher
# Create your views here.
# TODO:(1) Add a view that list all teacher.

# TODO:(2) Add a detail view for all teacher.


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
              'email', 'cellphone_number']