from django.shortcuts import render, reverse
from django.views.generic import DetailView, CreateView, UpdateView

from apps.auth.models import User 
from mysite.views import ListView
from .models import Teacher
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# TODO:(1) Add a view that list all teacher.
class TeacherList(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'modules/staff/teacher_list.html'
    context_object_name = 'teacher_list'
    paginate_by = 25
    base_url = 'staff:list'


# TODO:(2) Add a detail view for all teacher.
class TeacherDetail(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'modules/staff/teacher_detail.html'
    context_object_name = 'teacher'
