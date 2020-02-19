from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, default = "", on_delete=models.CASCADE)
    

# Create your models here.
