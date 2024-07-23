from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Breed, Dog


@admin.register(Breed)
class BreedAdmin(ModelAdmin):
    """Регистрация модели Breed в админпанеле."""

    list_display = (
        'id',
        'name',
        'size',
        'friendliness',
        'trainability',
        'shedding_amount',
        'exercise_needs'
    )
    list_editable = (
        'size',
        'friendliness',
        'trainability',
        'shedding_amount',
        'exercise_needs'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)


@admin.register(Dog)
class DogAdmin(ModelAdmin):
    """Регистрация модели Dog в админпанеле."""
    list_display = (
        'id',
        'name',
        'age',
        'breed',
        'gender',
        'color',
        'favorite_food',
        'favorite_toy'
    )
    list_editable = (
        'name',
        'age',
        'breed',
        'gender',
        'color',
        'favorite_food',
        'favorite_toy'
    )
    search_fields = ('name', 'age', 'breed')
    list_filter = ('name', 'breed')
    list_display_links = ('name', 'breed')
