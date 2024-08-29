# Generated by Django 4.2.10 on 2024-08-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_userprofile_user'),
        ('tradesman', '0012_alter_job_county_alter_job_other_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tradesman_assigned',
            field=models.ManyToManyField(blank=True, related_name='tradesman', to='main.userprofile'),
        ),
    ]
