from django.urls import path

from .views import Login, Logout, ChangePassword

app_name = 'auth'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('changepassword/<int:pk>', ChangePassword.as_view(), name='change-password')
]
