# Generated by Django 2.1.1 on 2018-09-15 05:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('attendance', '0010_auto_20180914_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workingday',
            old_name='lecture_attendances',
            new_name='lecture_attendance',
        ),
    ]