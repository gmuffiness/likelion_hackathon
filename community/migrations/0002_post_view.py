# Generated by Django 3.0.8 on 2020-09-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
