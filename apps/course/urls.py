from django.urls import path

from .views import CourseList, CourseDetail, CourseCreate, \
CourseUpdate, CourseDelete, SubjectDetail, SubjectView, SubjectDView, student_search, \
RegisterView


app_name = 'course'

urlpatterns = [
    path('', CourseList.as_view(), name='list'),
    path('add', CourseCreate.as_view(), name='create'),
    path('<int:pk>/update', CourseUpdate.as_view(), name='update'),
    path('<int:pk>/delete', CourseDelete.as_view(), name='delete'),
    path('<int:pk>', CourseDetail.as_view(), name='detail'),
    path('<int:pk>/subject/add', SubjectView.as_view(), name='create_subject'),
    path('<int:pk>/subject/delete', SubjectDView.as_view(), name='delete_subject'),
    path('<int:pk>/subject', SubjectDetail.as_view(), name='subject'),
    path('<int:pk>/studentsearch', student_search, name='student_search'),
    path('<int:pk>/student', RegisterView.as_view(), name='register'),
]
