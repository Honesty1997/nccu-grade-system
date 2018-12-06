from django.urls import path

from .views import edit_grade

app_name = 'grade'

urlpatterns = [
    path('edit/', edit_grade, name='edit')
]