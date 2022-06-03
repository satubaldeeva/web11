from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from datetime import date, datetime

from django.urls import reverse


class Account(models.Model):
    firstnameRegex = RegexValidator(regex=r"^([A-ZА-Я][a-zа-я]{3,11})$")
    firstname = models.CharField(validators=[firstnameRegex], max_length=20)
    messages = models.TextField('Messages')
    email = models.EmailField('Email')
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=12)

    def __str__(self):
        return "Имя пользователя: " + self.firstname + "\nПочта: " + str(self.email) + "\nТелефон: " + str(
            self.phone) + "\nMessages: " + str(self.messages) + "\n"


class Recipes(models.Model):
    title = models.CharField('Title', max_length=200)
    slug = models.SlugField('Slug', max_length=200)
    ingredients = models.TextField('Ingredients')
    recipe = models.TextField('Recipe')
    created = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    image3 = models.ImageField(upload_to='images')
    favourite = models.ManyToManyField(User, related_name="favourite", blank=True)

    def __str__(self):
        return self.title + self.ingredients + self.recipe

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
