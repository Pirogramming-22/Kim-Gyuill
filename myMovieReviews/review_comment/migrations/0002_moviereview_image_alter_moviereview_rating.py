# Generated by Django 5.1.4 on 2025-01-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviereview',
            name='image',
            field=models.ImageField(blank=True, help_text='이미지를 업로드하세요.', null=True, upload_to='review_images/'),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
