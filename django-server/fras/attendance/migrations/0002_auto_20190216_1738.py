# Generated by Django 2.1.3 on 2019-02-16 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectureattendance',
            name='end',
            field=models.DateField(default=datetime.datetime(2019, 2, 16, 17, 38, 32, 399680)),
        ),
        migrations.AlterField(
            model_name='lectureattendance',
            name='start',
            field=models.DateField(default=datetime.datetime(2019, 2, 16, 17, 38, 32, 399680)),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False,
                                      verbose_name='Identification Number'),
        ),
    ]
