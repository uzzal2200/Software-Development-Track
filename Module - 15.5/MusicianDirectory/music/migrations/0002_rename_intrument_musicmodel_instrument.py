# Generated by Django 5.0.6 on 2024-07-14 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicmodel',
            old_name='Intrument',
            new_name='Instrument',
        ),
    ]