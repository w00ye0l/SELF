from django.db import models

# Create your models here.
class Beacon(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    bluetooth_name = models.CharField(max_length=50)