# Generated by Django 5.0.6 on 2024-05-24 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='title',
            new_name='songName',
        ),
    ]
