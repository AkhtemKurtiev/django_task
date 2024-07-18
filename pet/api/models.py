from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .constants import BREED_SIZE_CHOICE


class Breed(models.Model):
    """Модель Порода."""

    name = models.CharField(max_length=255)
    size = models.CharField(
        max_length=7,
        choices=BREED_SIZE_CHOICE,
        default='Medium'
    )
    friendliness = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    trainability = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    shedding_amount = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    exercise_needs = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    def __str__(self):
        return f'Name of breed: {self.name}'


class Dog(models.Model):
    """Модель Собака."""

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        related_name='Dogs',
        null=True
    )
    gender = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)
    favorite_toy = models.CharField(max_length=255)

    def __str__(self):
        return f'Name of dog: {self.name}'
