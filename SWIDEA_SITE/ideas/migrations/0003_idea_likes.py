# Generated by Django 5.1.4 on 2025-01-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_idea_devtool'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
