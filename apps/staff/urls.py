from django.urls import path

from .views import TeacherList, TeacherDetail, \
TeacherCreate, TeacherUpdate

app_name = 'staff'

urlpatterns = [
    path('', TeacherList.as_view(), name='list'),
    path('<int:pk>', TeacherDetail.as_view(), name='detail'),
    path('create', TeacherCreate.as_view(), name='create'),
    path('<int:pk>/update', TeacherUpdate.as_view(), name='update'),
]
