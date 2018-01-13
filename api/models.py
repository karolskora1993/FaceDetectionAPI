from django.db import models
# Create your models here.


class Face(models.Model):

    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
