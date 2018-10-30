from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.shortcuts import redirect
# Create your views here.

class Login(LoginView):
    template_name = 'modules/auth/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')
