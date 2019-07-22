from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import FormView

from common.forms import RegisterUserForm


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
