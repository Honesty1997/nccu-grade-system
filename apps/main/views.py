from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.course.models import Course
from apps.student.models import Student
from apps.staff.models import Teacher
# Create your views here.
@login_required
def main(request):
    # TODO:
    # 如果request.user是學生，找出所有她們註冊的課程，然後assign到course_list。
    # 如果request.user是老師，找出所有他們教導的課程。
    # 如果是admin，就列出前10個最新的course就好。
    if request.user.role_field == 1:
        course_list = Student.objects.filter(email=request.user.account).get().course_set.all()
    elif request.user.role_field == 2:
        course_list = Teacher.objects.filter(email=request.user.account).get().course_set.all()
    elif request.user.role_field == 4:
        course_list = Course.objects.all()[:10]
    return render(request, 'modules/main/main.html', {'course_list': course_list})
