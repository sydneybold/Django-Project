from django.db import models
from users.models import Profile

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    caption = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption
