from django.db import models

# Create your models here.

class NpcInfo(models.Model):
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=32)
    hp = models.CharField(max_length=32)
    details = models.CharField(max_length=512,default="")



