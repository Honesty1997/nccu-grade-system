from django.urls import path

from .views import ListCourse, DetailCourse, DetailSubject

app_name = 'course'

urlpatterns = [
    path('', ListCourse.as_view(), name='list'),
    path('<int:pk>', DetailCourse.as_view(), name='detail'),
    path('subject/<int:pk>',
         DetailSubject.as_view(), name='subject'),
]
