# Generated by Django 3.2 on 2021-04-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_alter_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(verbose_name='Заметка'),
        ),
    ]
