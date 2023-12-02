from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Dictionary(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=256)
    url = models.URLField()
    tag = models.CharField(max_length=256)
    url_tag = models.CharField(max_length=2560,default=None)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

'''
class SlackBots(models.Model):
    botname = models.CharField(max_length=256)
    #tokun = 
'''