"""toas_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import TemplateView

from common.views import (
    LoginUserView,
    RegistrationView,
    UserProfileEditView,
    UserProfileView
)
from pictures.views import (
    EndlessPictureView,
    PicturePostUploadView
)

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # root site
    path("", EndlessPictureView.as_view(), name="root"),
    # User Views
    path("accounts/register/", RegistrationView.as_view(), name="user-register"),
    path("accounts/login/", LoginUserView.as_view(), name="user-login"),
    path("accounts/logout/", LogoutView.as_view(), name="user-logout"),
    path("accounts/my/profile/", UserProfileView.as_view(), name="user-profile"),
    path(
        "accounts/<int:pk>/profile/",
        UserProfileView.as_view(),
        name="user-profile-detail",
    ),
    path(
        "accounts/profile/edit/", UserProfileEditView.as_view(), name="user-profile-edit"
    ),
    # Pictures
    path("pictures/upload", PicturePostUploadView.as_view(), name="picture-post-upload")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
