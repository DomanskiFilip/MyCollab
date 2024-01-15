
from django.db import models

class CollabTag(models.Model):
    name = models.CharField(max_length=200)


class Collab(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(CollabTag)
    created_at = models.DateTimeField(auto_now_add=True)
    