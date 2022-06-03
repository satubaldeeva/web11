from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register, TranslationOptions
from .models import Account
from .models import Recipes
from modeltranslation.admin import TranslationAdmin


@register(Account)
class AccountTranslationOptions(TranslationOptions):
    fields = ('firstname', 'messages')


@register(Recipes)
class RecipesTranslationOptions(TranslationOptions):
    fields = ('title', 'ingredients','recipe')



