# Generated by Django 4.2.10 on 2024-02-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_userprofile_trade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.IntegerField(choices=[(0, 'Planner'), (1, 'Tradesman')], default=0),
        ),
    ]
