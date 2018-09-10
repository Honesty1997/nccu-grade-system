from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json

from .models import Grade
# Create your views here.
def edit_grade(request):
    if request.method == 'POST':
        form_data = json.loads(request.body)
        grade_id = form_data.get('pk')
        new_score = form_data.get('score')

        grade = get_object_or_404(Grade, pk=grade_id)
        grade.score = new_score
        grade.save()

        response = {
            'status': 'success',
            'score': grade.score,
            'new_average': grade.subject.average,
        }
        return JsonResponse(response)
