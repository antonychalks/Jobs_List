# Generated by Django 4.2.10 on 2024-02-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_userprofile_fname_alter_userprofile_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lname',
            field=models.CharField(max_length=50),
        ),
    ]