
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Drink


@receiver([post_save, post_delete], sender=Drink)
def invalidate_drink_cache(sender, instance, **kwargs):
    cache.delete('drinks')
