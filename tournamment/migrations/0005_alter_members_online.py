# Generated by Django 4.0.5 on 2022-12-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournamment', '0004_members_boss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
