
from django.db import models


class CollabTag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



class Collab(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(CollabTag)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    
    def __str__(self):
        return self.title
    
    def get_tags(self):
        return [tag.name for tag in self.tags.all()]
    