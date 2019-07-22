from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    """Sets an upload folder name for a user directory"""
    return f"users/{instance.user.id}/profile/{filename}"


class Profile(models.Model):
    """A user's profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.user.username} - profile"
