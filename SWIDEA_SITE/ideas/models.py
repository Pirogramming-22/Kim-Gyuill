from django.db import models
from tools.models import Tool
import os

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='idea_images/', blank=True, null=True, help_text="이미지를 업로드하세요.")
    content = models.TextField()
    interest = models.DecimalField(max_digits=10, decimal_places=1)
    devtool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True, related_name="ideas")
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)  # 이미지 파일 삭제
        super().delete(*args, **kwargs)  # 기본 삭제 동작 호출

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Idea.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)  # 기존 이미지 파일 삭제
        super().save(*args, **kwargs)  # 기본 저장 동작 호출