from django.db import models
from django.utils import timezone

class Post(models.Model):
    postname = models.CharField(max_length=100)
    relesedate = models.DateTimeField(blank=True, null=True)
    rt_point = models.CharField(max_length=10, blank=True, null=True, default='')
    #contents = models.URLField


    def __str__(self):
        return self.postname