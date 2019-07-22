from django import forms
from django.contrib.auth.forms import UserCreationForm

from common.models import Profile


class RegisterUserForm(UserCreationForm):
    """A form that registers a user"""

    def save(self):
        user = super().save(commit=True)
        # Save a profile object for the user
        profile = Profile(user=user)
        profile.save()

        return user


class UserProfileForm(forms.ModelForm):
    """Form for the user profile"""

    class Meta:
        model = Profile
        fields = ["photo", "bio"]
