from django import forms
from .models import Tool  

class UserForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ('__all__')