# Generated by Django 5.2.3 on 2025-07-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_quote_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quote',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
