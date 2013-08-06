from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=12,unique=True)
	nickname=models.CharField(max_length=20)
	description=models.TextField()
	img=models.URLField(unique=True)
	rank=models.IntegerField()
	last=models.DateTimeField(auto_now=True)
	
