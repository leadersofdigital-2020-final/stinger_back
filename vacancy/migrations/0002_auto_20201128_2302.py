# Generated by Django 3.1.3 on 2020-11-28 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='image',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='video',
        ),
    ]
