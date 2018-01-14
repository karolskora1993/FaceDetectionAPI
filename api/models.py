from django.db import models
# Create your models here.


class Face(models.Model):

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='faces/')
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
