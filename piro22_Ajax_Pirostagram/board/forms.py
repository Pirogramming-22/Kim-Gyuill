from django import forms
from .models import Board

class PostForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('image', 'content')
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("이미지를 반드시 첨부해야 합니다.")
        return image
