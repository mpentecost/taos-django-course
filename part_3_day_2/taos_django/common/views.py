from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from common.forms import RegisterUserForm, UserProfileForm
from common.models import Profile


class RegistrationView(FormView):
    """Registers new users"""

    template_name = "common/register.html"
    form_class = RegisterUserForm
    success_url = "/"

    def form_valid(self, form):
        """Save the user to the database"""
        user = form.save()
        # login the user
        login(self.request, user)
        return super().form_valid(form)


class LoginUserView(LoginView):
    """Logs in the user"""

    template_name = "common/login.html"
    success_url = "/"


class UserProfileView(TemplateView):
    """The user's profile"""
    template_name = "common/profile.html"

    def get_context_data(self, *args, **kwargs):
        """Add the profile object to the template context"""
        context = super().get_context_data(*args, **kwargs)

        # base case: non editable profiles e.g. looking at another user's profile
        user_pk = self.kwargs.get("pk", None)
        editable = False

        # get the pk if in the context, otherwise the request
        if not user_pk:
            user_pk = self.request.user.id
            editable = True

        profile = Profile.objects.get(user_id=user_pk)
        context["profile"] = profile
        context["editable"] = editable

        return context


class UserProfileEditView(FormView):
    """Updates the user's profile"""

    template_name = "common/profile-edit.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("user-profile")

    def form_valid(self, form):
        """Updates the user's profile in the DB"""
        cleaned_data = form.cleaned_data
        profile = Profile.objects.get(user=self.request.user)
        profile.bio = cleaned_data.get("bio", None)
        profile.photo = cleaned_data.get("photo", None)
        profile.save()

        return super().form_valid(form)
