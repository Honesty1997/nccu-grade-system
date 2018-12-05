from django.urls import path

from .views import StudentList, StudentDetail, \
StudentCreate, StudentUpdate, StudentCourseList

app_name = 'student'

urlpatterns = [
    path('', StudentList.as_view(), name='list'),
    path('<int:pk>', StudentDetail.as_view(), name='detail'),
    path('create', StudentCreate.as_view(), name='create'),
    path('<int:pk>/update', StudentUpdate.as_view(), name='update'),
    path('courselist/', StudentCourseList.as_view(), name='course_list'),
]
