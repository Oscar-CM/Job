from django.db import models
from django.utils import timezone

class Post(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    

# Create your models here.
