# Generated by Django 4.2.7 on 2024-02-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
