# Generated by Django 2.0.1 on 2018-01-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180114_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]