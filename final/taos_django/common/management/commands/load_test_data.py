import logging
import os
import random

from django.core.files import File
from django.core.management.base import BaseCommand

from common.factories import ProfileFactory
from pictures.factories import CommentFactory, PicturePostFactory

LOGGER = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Loads test data into the fotogram website.  
    Note: requires taos_django/test_data folder, make a copy of 
    the test data in the root folder to final/taos_django/test_data
    """

    def handle(self, *args, **options):
        # Create 50 User's w/ Profiles and a post each, with 10 random comments
        photos = os.listdir("/app/test_data/posts")

        for x in range(1, 51):
            profile = ProfileFactory()
            profile.photo.save(
                f"image-{x}.png",
                File(open(f"/app/test_data/profiles/image-{x}.png", "rb")),
            )
            LOGGER.debug("Created profile for %s", profile.user.username)

            picture_post = PicturePostFactory(user=profile.user)
            photo_filename = photos.pop()
            picture_post.photo.save(
                photo_filename,
                File(open(f"/app/test_data/posts/{photo_filename}", "rb")),
            )
            LOGGER.debug("Created Photo post for %s", profile.user.username)

            # add random # comments
            for y in range(0, random.randint(1, 5)):
                comment = CommentFactory(picture_post=picture_post)
                random_photo_index = random.randint(51, 200)
                comment.user.profile.photo.save(
                    f"image-{random_photo_index}.png",
                    File(
                        open(
                            f"/app/test_data/profiles/image-{random_photo_index}.png",
                            "rb",
                        )
                    ),
                )
                LOGGER.debug("comment left on post %d", picture_post.id)
