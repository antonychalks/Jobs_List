# Generated by Django 4.2.10 on 2024-03-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='county',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nok_number',
            field=models.CharField(blank=True, default='0', max_length=15, verbose_name='Next of Kin contact number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='other_phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Other Phone Number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='postcode',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='town_city',
            field=models.CharField(blank=True, max_length=20, verbose_name='Town/City'),
        ),
    ]
