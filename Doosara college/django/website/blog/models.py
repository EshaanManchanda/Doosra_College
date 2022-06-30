from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    authors=models.CharField(max_length=50)
    views=models.IntegerField()
    like=models.IntegerField()

