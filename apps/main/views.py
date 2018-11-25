from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.course.models import Course
from apps.auth.models import User
# Create your views here.
@login_required
def main(request):
    # TODO:
    # 如果request.user是學生，找出所有她們註冊的課程，然後assign到course_list。
    # 如果request.user是老師，找出所有他們教導的課程。
    # 如果是admin，就列出前10個最新的course就好。
    
    # if request.user.role_field == 1:
    #     stu_course = course.registered_student.objects.all(student_id == student_id)
    #     course_list = Course.objects.all(id in stu_course.course_id)
    # elif request.user.role_field == 2:
    #     course_list = Course.objects.all(teacher_id == request.user.id)
    # else:
    #     course_list = Course.objects.all()[:10]
    course_list = Course.objects.all()[:10]
    return render(request, 'modules/main/main.html', {'course_list': course_list})
