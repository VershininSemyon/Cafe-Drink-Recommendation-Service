
from django.contrib import admin

from .models import Drink


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'strength', 'sweetness', 'bitterness', 'temperature', 'caffeine_free', 'milk_based')
    list_filter = ('strength', 'sweetness', 'bitterness', 'temperature', 'caffeine_free', 'milk_based')
    search_fields = ('name', 'description')
