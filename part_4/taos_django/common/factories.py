from django.contrib.auth.models import User

import factory

from common.models import Profile


class UserFactory(factory.DjangoModelFactory):
    """Factory for user objects"""

    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = factory.Faker("user_name")
    # pw: djangocourse
    password = (
        "pbkdf2_sha256$150000$11yA44IWTUjb$mDO/y/+cOTSi+IO+8hPnFozGakND/r0v0Mcq+DtQNL8="
    )
    # related factory to Profile
    profile = factory.RelatedFactory("common.factories.ProfileFactory", "user")


class ProfileFactory(factory.DjangoModelFactory):
    """Factory for profile objects"""

    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory, profile=None)
    bio = factory.Faker("paragraph")
