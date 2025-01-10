from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['image', 'title', 'released_year', 'genre', 'rating', 'runtime', 'review', 'director', 'actor',]  # 'image' 추가

    def clean_released_year(self):
        year = self.cleaned_data['released_year']
        if not isinstance(year, int):
            raise forms.ValidationError('* 년도는 숫자여야 합니다. *')
        return year

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not (0 <= rating <= 5):
            raise forms.ValidationError('* 별점은 0~5 사이여야 합니다. *')
        return rating

    def clean_runtime(self):
        runtime = self.cleaned_data['runtime']
        if not isinstance(runtime, int):
            raise forms.ValidationError('* 러닝타임은 숫자여야 합니다. *')
        return runtime

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB 제한
                raise forms.ValidationError('* 이미지 파일은 5MB 까지 가능합니다. *')
            if not image.content_type.startswith('image/'):
                raise forms.ValidationError('* 유효한 이미지 파일만 업로드 가능합니다. *')
        return image
