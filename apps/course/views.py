from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from mysite.views import ListView
from .models import Course, ScoringSubject
from apps.student.models import Student
from .forms import ScoringSubjectForm
# Create your views here.

class CourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'modules/course/course.html'
    context_object_name = 'course_list'
    base_url = 'course:list'
    paginate_by = 25

class CourseDetail(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'modules/course/course_detail.html'
    contex_object_name = 'course'

class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'modules/common/form.html'
    fields = ['course_name', 'description', 'teacher']
    context_object_name = 'form'

class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'modules/common/form.html'
    fields = ['course_name', 'description']
    context_object_name = 'form'

class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('course:list')

class SubjectDetail(LoginRequiredMixin, DetailView):
    model = ScoringSubject
    template_name = 'modules/course/subject.html'
    context_object_name = 'subject'

class SubjectView(LoginRequiredMixin, View):
    def get(self, request, pk):
        form = ScoringSubjectForm()
        return render(request, 'modules/common/form.html', {'form': form})

    def post(self, request, pk):
        form = ScoringSubjectForm(request.POST)
        if form.is_valid():
            course = get_object_or_404(Course, pk=pk)
            subject, _ = course.add_new_subject(form.cleaned_data['title'])
            return redirect(subject)
        return render(request, 'modules/common/form.html', {'form': form})

class SubjectDView(LoginRequiredMixin, View):
    def get(self, request, pk):
            form = ScoringSubjectForm()
            return render(request, 'modules/common/form.html', {'form': form})
    
    def post(self, request, pk):
        form = ScoringSubjectForm(request.POST)
        if form.is_valid():
            course = get_object_or_404(Course, pk=pk)
            course.remove_existing_subject(form.cleaned_data['title'])
            return redirect('course:detail', pk=pk)
        return render(request, 'modules/common/form.html', {'form': form})

class RegisterView(LoginRequiredMixin, View):
    def get(self, request, pk):
        accept_type = request.META.get('HTTP_ACCEPT', 'text/html')
        course = get_object_or_404(Course, pk=pk)
        student_list = [student.info()
                        for student in course.registered_students.all()]
        if accept_type == 'application/json':
            return JsonResponse({'studentList': student_list})
        return render(request, 'modules/course/register.html', {'pk': pk, 'student_list': student_list})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        data = json.loads(request.body)
        student_number = data.get('student')
        student = get_object_or_404(Student, pk=student_number)
        course, count = course.register([student])
        response = {
            'status': 'success',
            'nAdded': count,
        }
        return JsonResponse(response)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        data = json.loads(request.body)
        student_number = data.get('student')
        student = get_object_or_404(Student, pk=student_number)
        course, count = course.unregister([student])
        response = {
            'status': 'success',
            'nRemoved': count,
        }
        return JsonResponse(response)

@login_required
def student_search(request, pk):
    course = get_object_or_404(Course, pk=pk)
    student_pk = request.GET.get('student', '')
    if not student_pk:
        response = {
            'status': 'failed.',
            'message': 'Student\'pk not provided.'
        }
        return JsonResponse(response)
    try:
        student = Student.objects.get(pk=student_pk)
    except Student.DoesNotExist:
        response = {
            'status': 'failed',
            'message': 'Student not found',
        }
        return JsonResponse(response, status=404)

    response = {
        'status': 'success',
        'student': student.info(),
    }

    return JsonResponse(response) 
