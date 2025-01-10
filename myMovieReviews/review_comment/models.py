from django.db import models


class MovieReview(models.Model):

    title = models.CharField(max_length=200)
    released_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50, choices=[
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('SF', 'SF'),
        ('Horror', 'Horror'),
    ])
    rating = models.DecimalField(max_digits=10, decimal_places=1)
    runtime = models.PositiveIntegerField(help_text="러닝타임을 분 단위로 입력하세요.")
    review = models.TextField()
    director = models.CharField(max_length=200)
    actor = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
