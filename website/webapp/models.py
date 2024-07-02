import datetime

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)
    enable = models.BooleanField(default=False)

    def is_enabled(self):
        return self.enable

    def __str__(self):
	    return f"{self.name}"

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published")
    hits_view = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
	    return f"{self.title}"

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published")
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)