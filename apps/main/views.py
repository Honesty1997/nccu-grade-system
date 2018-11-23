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
    if request.user.is_student:
        course_list = request.user.student.course_set.all()
        # course_list = Student.objects.get(email=request.user.account).course_set.all()
    elif request.user.is_teacher:
        course_list = request.user.teacher.course_set.all()
        # course_list = Teacher.objects.get(email=request.user.account).course_set.all()
    elif request.user.is_admin:
        course_list = Course.objects.all()[:10]
    return render(request, 'modules/main/main.html', {'course_list': course_list})
