from django.db import models

# Create your models here.
class homtab(models.Model):
    moviename=models.CharField(max_length=200)
    genere=models.CharField(max_length=200)
    add=models.ImageField(upload_to='uploaded')
    bool=models.BooleanField(default=False)
    desp=models.TextField()
    actor=models.CharField(max_length=200)
    actress=models.CharField(max_length=200)
