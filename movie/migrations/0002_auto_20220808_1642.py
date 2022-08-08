# Generated by Django 3.2.14 on 2022-08-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField(max_length=4)),
                ('movie', models.ManyToManyField(to='movie.Movie')),
            ],
        ),
        migrations.DeleteModel(
            name='Actors',
        ),
    ]