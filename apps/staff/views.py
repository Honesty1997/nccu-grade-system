from django.shortcuts import render, reverse

from apps.auth.models import User 
from core.views import ListView, DetailView, CreateView, UpdateView
from .models import Teacher
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# TODO:(1) Add a view that list all teacher.
class TeacherList(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'modules/staff/teacher_list.html'
    context_object_name = 'teacher_list'
    paginate_by = 25
    authorized_groups = ['admin']
    base_url = 'staff:list'


# TODO:(2) Add a detail view for all teacher.
class TeacherDetail(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'modules/staff/teacher_detail.html'
    authorized_groups = ['admin', 'teacher']
    context_object_name = 'teacher'


class TeacherCourseList(LoginRequiredMixin, ListView):
    template_name = 'modules/staff/teacher_course_list.html'
    paginate_by = 25
    base_url = 'staff:course_list'
    context_object_name = 'course_list'
    authorized_groups = ['teacher', 'admin']

    def get_queryset(self):
        return self.request.user.teacher.course_set.all()
