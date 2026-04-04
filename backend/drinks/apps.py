
from django.apps import AppConfig


class DrinksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drinks'

    def ready(self):
        from . import signals

        return super().ready()
