# Generated by Django 5.0.6 on 2024-07-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fahter_name',
            field=models.TextField(default='rahim'),
        ),
    ]