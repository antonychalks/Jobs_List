# Generated by Django 4.2.10 on 2024-09-10 15:58

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(0, 'Planner'), (1, 'Tradesman')], default=0)),
                ('trade', multiselectfield.db.fields.MultiSelectField(choices=[('Ca', 'Carpenter'), ('Pl', 'Plumber'), ('El', 'Electrician'), ('Pa', 'Plasterer'), ('Gw', 'Groundsworker'), ('De', 'Decorator'), ('Ga', 'Gas'), ('AD', 'Planner')], max_length=30)),
                ('profile_image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('fname', models.CharField(max_length=50, verbose_name='First name')),
                ('lname', models.CharField(max_length=50, verbose_name='Last name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('medical', models.TextField(blank=True, verbose_name='Medical Conditions')),
                ('nok', models.CharField(blank=True, max_length=50, verbose_name='Next of Kin')),
                ('nok_number', models.CharField(blank=True, max_length=15, verbose_name='Next of Kin contact number')),
                ('certifications', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('street', models.CharField(blank=True, max_length=40)),
                ('town_city', models.CharField(blank=True, max_length=20, verbose_name='Town/City')),
                ('county', models.CharField(blank=True, max_length=25)),
                ('postcode', models.CharField(blank=True, max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('other_phone', models.CharField(blank=True, max_length=15, verbose_name='Other Phone Number')),
                ('profile_complete', models.BooleanField(default=False)),
                ('is_initial_signup', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['role'],
            },
        ),
    ]
