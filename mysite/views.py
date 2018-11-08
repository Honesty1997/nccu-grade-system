from django.views.generic import ListView as LV
from django.shortcuts import render

class ListView(LV):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = self.base_url
        return context

def home_page(request):
    if request.user.is_authenticated():
        if user.is_student:
            pass
        return render(request, 'modules/index/index.html')

class OwnCourseListView(ListView):
    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter()