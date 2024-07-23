from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .constants import BREED_SIZE_CHOICE


class Breed(models.Model):
    """Модель Порода."""

    name = models.CharField('Название породы', max_length=255)
    size = models.CharField(
        'Размер',
        max_length=7,
        choices=BREED_SIZE_CHOICE,
        default='Medium'
    )
    friendliness = models.IntegerField(
        'Дружелюбность',
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    trainability = models.IntegerField(
        'Обучаемость',
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    shedding_amount = models.IntegerField(
        'Линька',
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    exercise_needs = models.IntegerField(
        'Активность',
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return f'Название породы: {self.name}'


class Dog(models.Model):
    """Модель Собака."""

    name = models.CharField('Кличка', max_length=255)
    age = models.IntegerField('Возраст')
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        related_name='Dogs',
        null=True,
        verbose_name='Порода'
    )
    gender = models.CharField('Пол', max_length=255)
    color = models.CharField('Цвет', max_length=255)
    favorite_food = models.CharField('Любимая еда', max_length=255)
    favorite_toy = models.CharField('Любимая игрушка', max_length=255)

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'

    def __str__(self):
        return f'Кличка собаки: {self.name}'
