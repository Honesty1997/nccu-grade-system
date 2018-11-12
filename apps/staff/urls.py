from django.urls import path

from .views import ProfessorList, ProfessorDetail, \
ProfessorCreate, ProfessorUpdate

app_name = 'staff'

urlpatterns = [
    path('', ProfessorList.as_view(), name='list'),
    path('<int:pk>', ProfessorDetail.as_view(), name='detail'),
    path('create', ProfessorCreate.as_view(), name='create'),
    path('<int:pk>/update', ProfessorUpdate.as_view(), name='update'),
]