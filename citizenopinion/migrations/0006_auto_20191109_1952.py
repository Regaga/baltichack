# Generated by Django 2.2.7 on 2019-11-09 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizenopinion', '0005_auto_20191109_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 19, 52, 34, 123594), verbose_name='Дата публикации'),
        ),
    ]
