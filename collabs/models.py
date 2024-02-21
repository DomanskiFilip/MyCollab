
from django.db import models
from django.contrib.auth.models import User


class CollabTag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Collab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(CollabTag)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    
    def get_tags(self):
        return [tag.name for tag in self.tags.all()]
    
    # normally django removed objects with foreign keys on the database level which wouldnt call the delete method in Image object
    # overwriting the delete method to use orm:
    def delete(self, *args, **kwargs):
        for image in self.images.all():
            image.delete()
        super().delete(*args, **kwargs)
    
    
class CollabImage(models.Model):
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    is_main = models.BooleanField(default=False)
    description_img = models.TextField()

    def __str__(self):
        return f'Image for {self.collab.title}'
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)