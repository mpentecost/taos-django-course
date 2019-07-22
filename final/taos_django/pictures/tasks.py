from celery import shared_task
from pictures.models import PicturePost
import logging

LOGGER = logging.getLogger(__name__)

@shared_task
def process_like(pk):
    """Update the like"""
    
    picture_post = PicturePost.objects.get(pk=pk)
    picture_post.num_likes += 1
    picture_post.save()
