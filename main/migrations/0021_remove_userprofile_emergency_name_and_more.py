# Generated by Django 4.2.10 on 2024-02-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_address_ln_3_userprofile_county_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='emergency_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='emergency_number',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nok',
            field=models.CharField(blank=True, max_length=50, verbose_name='Next of Kin'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nok_number',
            field=models.CharField(blank=True, default='0', verbose_name='Next of Kin contact number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fname',
            field=models.CharField(max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lname',
            field=models.CharField(max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='medical',
            field=models.TextField(blank=True, verbose_name='Medical Conditions'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='other_phone',
            field=models.CharField(blank=True, verbose_name='Other Phone Number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='town_city',
            field=models.CharField(blank=True, verbose_name='Town/City'),
        ),
    ]
