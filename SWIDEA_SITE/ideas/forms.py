from django import forms
from .models import Idea

class PostForm(forms.ModelForm):
  class Meta:
    model= Idea
    fields = ('__all__')