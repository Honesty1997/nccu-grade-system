from django.views.generic import ListView as LV, View as V
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

class ListView(LV):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = self.base_url
        return context