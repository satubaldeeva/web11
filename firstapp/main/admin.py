from django.contrib import admin
from .models import Recipes
from .models import Account

from modeltranslation.admin import TranslationAdmin


@admin.register(Account)
class AccountAdmin(TranslationAdmin):
    pass


@admin.register(Recipes)
class RecipesAdmin(TranslationAdmin):
    pass


