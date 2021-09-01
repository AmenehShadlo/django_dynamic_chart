from django import forms
from django.db.models import fields
from .models import LessionScore

class LessionForm(forms.ModelForm):
    class Meta:
        model=LessionScore
        fields='__all__'