# Generated by Django 4.2.6 on 2023-10-18 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_celebration_mode', '0002_rename_events_eventss'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eventss',
            new_name='EventModel',
        ),
    ]