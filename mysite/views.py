from django.views.generic import ListView as LV

class ListView(LV):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = self.base_url
        return context
