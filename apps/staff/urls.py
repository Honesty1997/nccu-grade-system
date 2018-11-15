from django.urls import path

from .views import TeacherList, TeacherDetail

app_name = 'staff'

urlpatterns = [
    path('', TeacherList.as_view(), name='list'),
    path('<int:pk>', TeacherDetail.as_view(), name='detail'),
    # path('create', StudentCreate.as_view(), name='create'),
    # path('<int:pk>/update', StudentUpdate.as_view(), name='update'),
]
