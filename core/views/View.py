from django.views.generic import View as V
from django.http import JsonResponse, HttpResponse

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
        if request.META.get('HTTP_ACCEPT', '') == 'application/json':
            message = {
                'status': 'error',
                'message': 'Not authorized.'
            }
            return JsonResponse(message, status=403)
        return HttpResponse('Not allowed', status=403)