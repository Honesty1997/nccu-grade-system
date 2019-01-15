from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from .View import View
class DeleteView(View):
    model = None
    success_url = None
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
            if request.META.get('HTTP_ACCEPT', '') == 'application/json':
                return JsonResponse({'message': error_status['message']}, status=error_status['status_code'])
            return HttpResponse(error_status['message'], status=error_status['status_code'])

        if request.META.get('HTTP_ACCEPT', '') == 'application/json':
            response = {
                'message': 'success',
                'success_url': self.get_success_url(),
            }

            return JsonResponse(response)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.success_url
