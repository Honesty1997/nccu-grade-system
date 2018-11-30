from django.views.generic import ListView as LV, View as V
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

class ListView(LV):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = self.base_url
        return context

class OwnCourseListView(ListView):
    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter()

class View(V):
    AUTHORIZED_LEVEL = {
        'admin': 'is_admin',
        'teacher': 'is_teacher',
        'student': 'is_student',
        'executive': 'is_executive',
    }
    def dispatch(self, request, *args, **kwargs):
        authorized_groups = getattr(self, 'authorized_groups', ['student'])
        for group in authorized_groups:
            if getattr(request.user, View.AUTHORIZED_LEVEL[group]):
                return super().dispatch(request, *args, **kwargs)
        if request.META['HTTP_ACCEPT'] == 'application/json':
            message = {
                'status': 'error',
                'message': 'Not authorized.'
            }
            return JsonResponse(message, status=403)
        return HttpResponse('Not allowed', status=403)

class DeleteView(View):
    def delete(self, request, pk, *args, **kwargs):
        obj = None
        error_status = None
        try:
            obj = self.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            error_status = {
                'status_code': 404,
                'message': 'Not Found.',
            }

        if obj:
            try:
                obj.delete()
            except:
                error_status = {
                'status_code': 500,
                'message': 'Internal server error.',
            }
        if error_status:
            if request.META['HTTP_ACCEPT'] == 'application/json':
                return JsonResponse({'message': error_status['message']}, status=error_status['status_code'])
            return HttpResponse(error_status['message'], status=error_status['status_code'])

        if request.META['HTTP_ACCEPT'] == 'application/json':
            response = {
                'message': 'success',
                'success_url': self.get_success_url(),
            }

            return JsonResponse(response)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.success_url