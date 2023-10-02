from modeltranslation.translator import register, TranslationOptions
from .models import Category, Products, Review


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ("title", "description", "composition")


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ("name", "text")
