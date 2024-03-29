# Generated by Django 4.0.4 on 2022-05-22 12:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('ingredients', models.CharField(max_length=200, verbose_name='Ingredients')),
                ('recipe', models.CharField(max_length=200, verbose_name='Recipe')),
                ('image1', models.ImageField(upload_to='uploads/')),
                ('image2', models.ImageField(upload_to='uploads/')),
                ('image3', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')]),
        ),
    ]
