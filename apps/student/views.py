from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.auth.models import User 
from core.views import ListView, View, DetailView, CreateView, UpdateView
from .models import Student
from apps.course.models import Course

# Create your views here.
class StudentList(LoginRequiredMixin, ListView, View):
    model = Student
    template_name = 'modules/student/student_list.html'
    context_object_name = 'student_list'
    paginate_by = 25
    base_url = 'student:list'
    authrized_groups = ['admin', 'student']
class StudentDetail(LoginRequiredMixin, DetailView, View):
    model = Student
    template_name = 'modules/student/student_detail.html'
    context_object_name = 'student'
    authrized_groups = ['admin', 'student']

class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'phone_number']
    authrized_groups = ['admin']

class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number']
    authrized_groups = ['admin']

class StudentCourseList(LoginRequiredMixin, ListView):
    template_name = 'modules/student/student_course_list.html'
    paginate_by = 25
    base_url = 'student:course_list'
    context_object_name = 'course_list'
    authorized_groups = ['student']
    def get_queryset(self):
        return self.request.user.student.course_set.all()

class StudentCourseSubjectList(LoginRequiredMixin, View):
    authorized_groups = ['student']
    def get(self, request):
        pass