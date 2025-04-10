from django import forms
from .models import Knyga

class KnygaForm(forms.ModelForm):
    class Meta:
        model = Knyga
        fields = '__all__'