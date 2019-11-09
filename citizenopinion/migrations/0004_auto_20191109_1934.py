# Generated by Django 2.2.7 on 2019-11-09 16:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizenopinion', '0003_auto_20191109_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Post_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='citizenopinion.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='couner',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 19, 34, 27, 452291), verbose_name='Дата публикации'),
        ),
    ]