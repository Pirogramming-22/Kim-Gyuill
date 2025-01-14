from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='idea_images/', blank=True, null=True, help_text="이미지를 업로드하세요.")
    content = models.TextField()
    interest = models.DecimalField(max_digits=10, decimal_places=1)
    devtool = models.TextField()

    def __str__(self):
        return self.title
    