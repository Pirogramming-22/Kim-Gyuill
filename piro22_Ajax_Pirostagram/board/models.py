import os
from django.db import models

class Board(models.Model):
    image = models.ImageField(
        'Image:',
        upload_to='upload_images/',
        blank=True,
        null=False
    )
    content = models.TextField('게시물 내용:', default="")
    location = models.CharField(max_length=200, default=" ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")
    like = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # 기존 이미지를 교체할 경우 삭제
        if self.pk:
            old_instance = Board.objects.filter(pk=self.pk).first()
            if old_instance and old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # 이미지 삭제
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.pk)
