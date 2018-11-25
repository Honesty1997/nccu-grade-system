from django.forms import ModelForm

from .models import ScoringSubject

class ScoringSubjectForm(ModelForm):
    class Meta:
        model = ScoringSubject
        fields = ['title', 'subject_type']
