from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=10000)
    publish_date = models.DateTimeField()

