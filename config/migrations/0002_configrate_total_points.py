# Generated by Django 4.0.5 on 2023-01-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configrate',
            name='total_points',
            field=models.IntegerField(default=5000),
        ),
    ]
