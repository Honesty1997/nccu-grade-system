from django.urls import path

from .views import StudentList, StudentDetail

app_name = 'student'

urlpatterns = [
    path('', StudentList.as_view(), name='list'),
    path('<int:pk>', StudentDetail.as_view(), name='detail'),
]
