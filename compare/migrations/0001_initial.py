# Generated by Django 3.1.3 on 2020-11-29 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=300)),
                ('video', models.CharField(max_length=100)),
                ('stage', models.PositiveIntegerField(default=0)),
                ('schedule', models.PositiveIntegerField()),
                ('employment', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField()),
                ('experience', models.PositiveIntegerField(default=0)),
                ('skills', models.CharField(max_length=100)),
                ('achievements', models.CharField(blank=True, max_length=300)),
                ('expectations', models.CharField(max_length=100)),
                ('add_info', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=100)),
                ('rating', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
