# Generated by Django 3.0.2 on 2020-05-11 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200511_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]