from .models import Ex
from django.forms import ModelForm


class ExForm(ModelForm):
    class Meta:
        model = Ex
        fields = ['title', 'memo', 'important']
