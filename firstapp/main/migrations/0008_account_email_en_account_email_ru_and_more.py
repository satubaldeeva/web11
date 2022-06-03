# Generated by Django 4.0.4 on 2022-05-27 16:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_recipes_ingredients_alter_recipes_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email_en',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='account',
            name='email_ru',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='account',
            name='firstname_en',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex='^([A-ZА-Я][a-zа-я]{3,11})$')]),
        ),
        migrations.AddField(
            model_name='account',
            name='firstname_ru',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex='^([A-ZА-Я][a-zа-я]{3,11})$')]),
        ),
        migrations.AddField(
            model_name='account',
            name='messages_en',
            field=models.TextField(null=True, verbose_name='Messages'),
        ),
        migrations.AddField(
            model_name='account',
            name='messages_ru',
            field=models.TextField(null=True, verbose_name='Messages'),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_en',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')]),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_ru',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')]),
        ),
    ]