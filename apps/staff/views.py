from django.shortcuts import render, reverse
from django.views.generic import DetailView, CreateView, UpdateView

from apps.auth.models import User 
from mysite.views import ListView
from .models import Professor
# Create your views here.
class ProfessorList(ListView):
    model = Professor
    template_name = 'modules/staff/professor_list.html'
    context_object_name = 'professor_list'
    paginate_by = 25
    base_url = 'staff:list'

class ProfessorDetail(DetailView):
    model = Professor
    template_name = 'modules/staff/professor_detail.html'
    context_object_name = 'professor'


class ProfessorCreate(CreateView):
    model = Professor
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number', 'phone_number']
    base_url = 'staff:create'

class ProfessorUpdate(UpdateView):
    model = Professor
    template_name = 'modules/common/form.html'
    context_object_name = 'form'
    fields = ['first_name', 'last_name', 'address',
              'email', 'cellphone_number','phone_number']
    base_url = 'staff:update'

