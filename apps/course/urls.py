from django.urls import path

from .views import CourseList, CourseDetail, CourseCreate, \
CourseUpdate, CourseDelete, SubjectDetail, SubjectView, SubjectDelete, student_search, \
    RegisterView, SubjectScoreView


app_name = 'course'

urlpatterns = [
    path('', CourseList.as_view(), name='list'),
    path('add', CourseCreate.as_view(), name='create'),
    path('<int:pk>/update', CourseUpdate.as_view(), name='update'),
    path('<int:pk>/delete', CourseDelete.as_view(), name='delete'),
    path('<int:pk>', CourseDetail.as_view(), name='detail'),
    path('<int:pk>/subject/add', SubjectView.as_view(), name='create_subject'),
    path('<int:pk>/subject/<int:subject_pk>/delete', SubjectDelete.as_view(), name='delete_subject'),
    path('subject/<int:pk>', SubjectDetail.as_view(), name='subject'),
    path('studentsearch/<int:pk>', student_search, name='student_search'),
    path('student/<int:pk>', RegisterView.as_view(), name='register'),
    path('subject/<int:pk>/scores',
         SubjectScoreView.as_view(), name='subject_score'),
]
