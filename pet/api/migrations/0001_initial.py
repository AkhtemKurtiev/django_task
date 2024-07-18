# Generated by Django 5.0.7 on 2024-07-18 06:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Medium', max_length=7)),
                ('friendliness', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('trainability', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('shedding_amount', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('exercise_needs', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('favorite_food', models.CharField(max_length=255)),
                ('favorite_toy', models.CharField(max_length=255)),
                ('breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Dogs', to='api.breed')),
            ],
        ),
    ]
