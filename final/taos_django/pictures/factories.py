from django.contrib.auth.models import User

import factory

from common.factories import UserFactory
from pictures.models import Comment, PicturePost


class PicturePostFactory(factory.DjangoModelFactory):
    """Factory for PicturePost model"""

    class Meta:
        model = PicturePost

    user = factory.SubFactory(UserFactory)
    description = factory.Faker("paragraph")
    num_likes = factory.Faker("pyint", max_value=100)


class CommentFactory(factory.DjangoModelFactory):
    """Factory for Comment Factory"""

    class Meta:
        model = Comment

    picture_post = factory.SubFactory(PicturePostFactory)
    user = factory.SubFactory(UserFactory)
    message = factory.Faker("paragraph")
