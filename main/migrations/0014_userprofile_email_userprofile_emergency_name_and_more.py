# Generated by Django 4.2.10 on 2024-02-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_userprofile_address_ln_1_userprofile_address_ln_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emergency_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emergency_number',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='medical',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='other_phone',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]
