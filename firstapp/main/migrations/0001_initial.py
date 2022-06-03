# Generated by Django 4.0.4 on 2022-05-21 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^([A-ZА-Я][a-zа-я]{3,11})$')])),
                ('messages', models.TextField(verbose_name='Messages')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^[+][0-9\\s]*$')])),
            ],
        ),
    ]
