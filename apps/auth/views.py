from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.shortcuts import redirect
# Create your views here.
from .models import User
from .forms import ChangePasswordForm
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


class ChangePassword(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = ChangePasswordForm()
        return render(request, 'modules/auth/change_password.html', { 'form': form })

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['password']
            user.set_password(new_password)
            user.save()
            if not request.user.is_admin:
                logout(request)
            return HttpResponseRedirect(reverse('main:homepage'))
        else:
            return render(request, 'modules/auth/change_password.html', { 'form': form })
