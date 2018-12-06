from django.urls import path

from .views import StudentList, StudentDetail, \
StudentCreate, StudentUpdate, StudentCourseList, \
StudentCourseSubjectList

app_name = 'student'

urlpatterns = [
    path('', StudentList.as_view(), name='list'),
    path('<int:pk>', StudentDetail.as_view(), name='detail'),
    path('create', StudentCreate.as_view(), name='create'),
    path('<int:pk>/update', StudentUpdate.as_view(), name='update'),
    path('course/', StudentCourseList.as_view(), name='course_list'),
    path('course/<int:course_pk>', StudentCourseSubjectList.as_view(), name='subject_list')
]
