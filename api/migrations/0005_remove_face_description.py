# Generated by Django 2.0.1 on 2018-01-16 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180114_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face',
            name='description',
        ),
    ]
