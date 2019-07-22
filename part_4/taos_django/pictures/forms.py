from django import forms

from pictures.models import PicturePost

class PicturePostForm(forms.ModelForm):
    """Form for uploading the picture post"""

    class Meta:
        model = PicturePost
        fields = ["photo", "description"]
