# Generated by Django 3.2 on 2021-04-10 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_note_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='date',
        ),
        migrations.RemoveField(
            model_name='note',
            name='task',
        ),
    ]