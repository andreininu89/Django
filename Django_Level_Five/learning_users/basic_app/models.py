from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes you want
    portfolio = models.URLField(max_length=200, blank=True)
    picture = models.ImageField(upload_to="profile_pics/", blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User!
        return self.user.username
