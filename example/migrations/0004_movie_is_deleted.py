# Generated by Django 2.2 on 2019-09-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_movie_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
