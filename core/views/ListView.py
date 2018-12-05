from django.views.generic import ListView as LV
from .View import View
class ListView(LV, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = self.base_url
        return context