# Generated by Django 5.1.4 on 2025-01-15 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ideas', to='tools.tool'),
        ),
    ]
