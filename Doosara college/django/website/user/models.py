from django.db import models

# Create your models here.
class user(models.Model):
    password=models.CharField(max_length=15)
    phone_no=models.IntegerField()
    email=models.EmailField()
    prof_desc=models.CharField(max_length=50)