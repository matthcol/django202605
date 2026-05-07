import logging

from django.db.models.signals import (
    pre_save, post_save,
    pre_delete, post_delete
)
from django.dispatch import receiver

from .models import Movie

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Movie)
def log_movie_created(sender, instance, created, **kwargs):
    if created:
        logger.info("Movie added: '%s' (%s)", instance.title, instance.year)
