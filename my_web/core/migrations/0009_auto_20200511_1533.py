# Generated by Django 3.0.2 on 2020-05-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200511_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(max_length=9),
        ),
    ]
