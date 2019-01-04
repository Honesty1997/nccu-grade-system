from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse

from apps.auth.models import User 
from core.views import ListView, View, DetailView, CreateView, UpdateView
from .models import Student
from apps.course.models import Course

# Create your views here.
class StudentList(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'modules/student/student_list.html'
    context_object_name = 'student_list'
    paginate_by = 25
    base_url = 'student:list'
    authorized_groups = ['admin']

class StudentDetail(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'modules/student/student_detail.html'
    context_object_name = 'student'
    authorized_groups = ['admin', 'student']

class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'phone_number']
    authorized_groups = ['admin']

class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number']
    authorized_groups = ['admin']

class StudentCourseList(LoginRequiredMixin, ListView):
    template_name = 'modules/student/student_course_list.html'
    paginate_by = 25
    base_url = 'student:course_list'
    context_object_name = 'course_list'
    authorized_groups = ['student', 'admin']
    def get_queryset(self):
        return self.request.user.student.course_set.all()

class StudentCourseSubjectList(LoginRequiredMixin, View):
    template_name = 'modules/student/student_course_detail.html'
    authorized_groups = ['student', 'admin']

    def get(self, request, course_pk):
        course = get_object_or_404(Course, pk=course_pk)
        if request.user.student not in course.registered_students.all():
            raise Http404
        if request.META['HTTP_ACCEPT'] == 'application/json':
            return JsonResponse({'results': course.get_total_score(request.user.student)})
        return render(request, self.template_name, {})
