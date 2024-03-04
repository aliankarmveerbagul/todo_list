from django import forms
from .models import to_data

class taskform(forms.ModelForm):
    class Meta:
        model = to_data
        fields = "__all__"

