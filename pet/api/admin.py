from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Breed, Dog


@admin.register(Breed)
class BreedAdmin(ModelAdmin):
    """Регистрация модели Breed в админпанеле."""


@admin.register(Dog)
class DogAdmin(ModelAdmin):
    """Регистрация модели Dog в админпанеле."""
