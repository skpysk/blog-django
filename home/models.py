from ast import mod
from django.db import models

# Create your models here.

class contacts(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,default="")
    email = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=13,default="")
    msg = models.CharField(max_length=255,default="")
    timstamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "message from " + self.name
    
    