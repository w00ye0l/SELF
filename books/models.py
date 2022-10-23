from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="book_img/")
    x = models.IntegerField()
    y = models.IntegerField()
