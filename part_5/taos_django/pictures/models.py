from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    """Sets an upload folder name for a user directory"""
    return f"users/{instance.user.id}/posts/{filename}"


class PicturePost(models.Model):
    """A user's post"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    num_likes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        """The PicturePost ID and Username"""
        return f"Post {self.id} - by {self.user.username}"


class Comment(models.Model):
    """A Post's comment"""

    picture_post = models.ForeignKey(
        PicturePost, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=144)

    def __str__(self):
        """The Comment ID and Username"""
        return f"Comment: {self.id} - by {self.user.username}"
