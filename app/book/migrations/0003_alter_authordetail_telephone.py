# Generated by Django 3.2.14 on 2022-08-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220808_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='telephone',
            field=models.BigIntegerField(blank=True, default='-', null=True),
        ),
    ]