from django.db import models
from review_comment.models import MovieReview


class Comment(models.Model):
    board = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)