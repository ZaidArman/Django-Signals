from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=50, default='')
    count = models.IntegerField(default=0)
    
class Post(models.Model):
    title = models.CharField(max_length=100, default='')
