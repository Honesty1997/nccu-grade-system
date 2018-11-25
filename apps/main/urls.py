from django.urls import path

from .views import main

app_name = 'main'

urlpatterns = [
    path('', main, name='homepage'),
]
