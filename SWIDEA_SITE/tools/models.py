from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=200)
    type = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.name