from django.urls import path

from .views import TeacherList, TeacherDetail, TeacherCourseList

app_name = 'staff'

urlpatterns = [
    path('', TeacherList.as_view(), name='list'),
    path('<int:pk>', TeacherDetail.as_view(), name='detail'),
    path('course/', TeacherCourseList.as_view(), name='course_list'),
    # path('<int:pk>/update', StudentUpdate.as_view(), name='update'),
]
