from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


class MovieReview(models.Model):
    image = models.ImageField(upload_to='review_images/', blank=True, null=True, help_text="이미지를 업로드하세요.")
    title = models.CharField(max_length=200)
    released_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50, choices=[
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('SF', 'SF'),
        ('Horror', 'Horror'),
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Animation', 'Animation'),
    ])
    rating = models.DecimalField(max_digits=10, decimal_places=1)
    runtime = models.PositiveIntegerField(help_text="러닝타임을 분 단위로 입력하세요.")
    review = models.TextField()
    director = models.CharField(max_length=200)
    actor = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 게시물 삭제 시 이미지 데이터도 같이 삭제
@receiver(post_delete, sender=MovieReview)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)


# 이미지 업데이트시 기존 이미지 데이터 삭제
@receiver(pre_save, sender=MovieReview)
def delete_old_image(sender, instance, **kwargs):
    if not instance.pk:  # 새로 생성되는 객체는 처리하지 않음
        return

    try:
        old_instance = MovieReview.objects.get(pk=instance.pk)
    except MovieReview.DoesNotExist:
        return

    # 새 이미지가 설정되고, 기존 이미지가 있는 경우 삭제
    if old_instance.image and old_instance.image != instance.image:
        old_image_path = old_instance.image.path
        if os.path.isfile(old_image_path):
            os.remove(old_image_path)
