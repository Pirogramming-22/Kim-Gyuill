from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'released_year', 'genre', 'rating', 'runtime', 'review', 'director', 'actor']

    def clean_released_year(self):
        year = self.cleaned_data['released_year']
        if not isinstance(year, int):
            raise forms.ValidationError('* 년도는 숫자여야 합니다. *')
        return year

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not (0 <= rating <= 5):
            raise forms.ValidationError('* 별점은 0~5 입니다. *')
        return rating

    def clean_runtime(self):
        runtime = self.cleaned_data['runtime']
        if not isinstance(runtime, int):
            raise forms.ValidationError('* 러닝타임은 숫자여야 합니다. *')
        return runtime
