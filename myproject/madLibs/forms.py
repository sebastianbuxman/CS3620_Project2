from django import forms
from .models import MadLib

class MadLibForm(forms.ModelForm):
    class Meta:
        model = MadLib
        fields = ['adjective1', 'place1', 'verb1', 'noun1', 'adjective2', 'verb2', 'noun2']
