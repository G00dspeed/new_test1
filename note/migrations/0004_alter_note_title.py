# Generated by Django 3.2 on 2021-04-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20210410_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(verbose_name='Заметка'),
        ),
    ]
