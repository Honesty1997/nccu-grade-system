from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

class Login(LoginView):
    template_name = 'modules/auth/login.html'
    redirect_authenticated_user = True


class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')
