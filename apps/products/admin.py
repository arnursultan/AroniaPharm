from django.contrib import admin
from .models import Products, Review, Category


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "clickable_title", "formatted_price", "date")
    list_display_links = ("clickable_title",)
    fields = (
        "image",
        "category",
        "title",
        "title_EN",
        "title_KY",
        "description",
        "description_EN",
        "description_KY",
        "composition",
        "composition_EN",
        "composition_KY",
        "price",
    )
    list_filter = ("category", "title", "description", "composition", "price")
    date_hierarchy = "date"

    def formatted_price(self, obj):
        return f"{int(obj.price):.0f}"

    formatted_price.short_description = "Цена"

    def clickable_title(self, obj):
        return obj.title

    clickable_title.short_description = "Название"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "text")
    fields = (
        "criteria_image",
        "name",
        "name_EN",
        "name_KY",
        "text",
        "text_EN",
        "text_KY",
    )
    list_filter = ("id", "name", "text")
    list_display_links = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("name", "name_EN", "name_KY")
    list_filter = ("id", "name")
    list_display_links = ("name",)
