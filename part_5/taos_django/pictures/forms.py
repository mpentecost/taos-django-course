from django import forms

from pictures.models import Comment, PicturePost


class PicturePostForm(forms.ModelForm):
    """Form for the user profile"""

    class Meta:
        model = PicturePost
        fields = ["photo", "description"]


class CommentForm(forms.ModelForm):
    """Form for a post's comment"""

    class Meta:
        model = Comment
        fields = ["message"]
