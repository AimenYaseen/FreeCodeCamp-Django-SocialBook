from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    This model has extra information about user which is not included in
    Django's default model.
    It has many-to-one relationship with user model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    token = models.IntegerField()
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images', default='default_user_image.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        self.user.username
