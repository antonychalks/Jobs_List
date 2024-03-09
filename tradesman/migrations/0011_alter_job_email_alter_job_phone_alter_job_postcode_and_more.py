# Generated by Django 4.2.10 on 2024-03-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradesman', '0010_alter_task_options_alter_job_job_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='job',
            name='phone',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='postcode',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.IntegerField(choices=[(0, 'Unassigned'), (1, 'Pending Start'), (2, 'In Progress'), (3, 'Completed')], verbose_name='Job Status'),
        ),
        migrations.AlterField(
            model_name='job',
            name='street',
            field=models.CharField(),
        ),
    ]
