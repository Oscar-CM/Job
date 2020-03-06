from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from jobs.models import Post


class Application(models.Model):
    title = models.CharField(max_length=50)
    profile = models.TextField()
    cv = models.FileField(upload_to = 'media/')
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title




# Create your models here.
