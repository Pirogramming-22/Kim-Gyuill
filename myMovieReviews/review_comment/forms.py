from django import forms
from .models import MovieReview


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = '__all__'
        labels = {
            'title': '제목',
            'released_year': '개봉 연도',
            'genre': '장르',
            'rating': '평점',
            'runtime': '러닝타임',
            'review': '리뷰',
            'director': '감독',
            'actor': '배우',
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and (rating < 0 or rating > 5):  # DecimalField의 범위 제한
            raise forms.ValidationError('별점은 0에서 5 사이여야 합니다.')
        return rating

