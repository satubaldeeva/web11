# Generated by Django 4.0.4 on 2022-05-22 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_recipes_image1_alter_recipes_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
