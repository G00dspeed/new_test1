# Generated by Django 3.2 on 2021-04-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_alter_note_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(),
        ),
    ]
