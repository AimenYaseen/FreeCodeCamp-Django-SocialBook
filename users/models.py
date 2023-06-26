from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    user_id = models.IntegerField()
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images', default='default_user_image.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        self.user.username
