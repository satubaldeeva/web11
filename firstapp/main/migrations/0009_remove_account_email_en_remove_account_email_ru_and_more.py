# Generated by Django 4.0.4 on 2022-05-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_account_email_en_account_email_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email_en',
        ),
        migrations.RemoveField(
            model_name='account',
            name='email_ru',
        ),
        migrations.RemoveField(
            model_name='account',
            name='phone_en',
        ),
        migrations.RemoveField(
            model_name='account',
            name='phone_ru',
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients_en',
            field=models.TextField(null=True, verbose_name='Ingredients'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients_ru',
            field=models.TextField(null=True, verbose_name='Ingredients'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
    ]