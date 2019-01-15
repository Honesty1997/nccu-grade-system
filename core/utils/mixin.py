from django.http import JsonResponse, HttpResponse

class CourseOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if request.user.is_teacher:
            course = self.model.objects.get(pk=pk)
            if not course.teacher == request.user.teacher:
                if request.META.get('HTTP_ACCEPT', '') == 'application/json':
                    message = {
                        'status': 'error',
                        'message': 'Not authorized.'
                    }
                    return JsonResponse(message, status=403)
                return HttpResponse('Not allowed', status=403)
        return super().dispatch(request, *args, **kwargs)

class SubjectOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('subject_pk')
        if request.user.is_teacher:
            subject = self.model.objects.get(pk=pk)
            if not subject.course.teacher == request.user.teacher:
                if request.META.get('HTTP_ACCEPT', '') == 'application/json':
                    message = {
                        'status': 'error',
                        'message': 'Not authorized.'
                    }
                    return JsonResponse(message, status=403)
                return HttpResponse('Not allowed', status=403)
        return super().dispatch(request, *args, **kwargs)
