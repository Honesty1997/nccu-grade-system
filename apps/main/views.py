from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.course.models import Course
from apps.student.models import Student
from apps.staff.models import Teacher
# Create your views here.
@login_required
def main(request):
    if request.user.is_student:
        course_list = request.user.student.course_set.all()
        # course_list = Student.objects.get(email=request.user.account).course_set.all()
    elif request.user.is_teacher:
        course_list = request.user.teacher.course_set.all()
        # course_list = Teacher.objects.get(email=request.user.account).course_set.all()
    elif request.user.is_admin:
        course_list = Course.objects.all()[:10]
    return render(request, 'modules/main/main.html', {'course_list': course_list})
