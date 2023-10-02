from rest_framework import serializers
from .models import Products, Review, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "name_EN", "name_KY"]


class ProductsSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.StringRelatedField(source="category", read_only=True)

    class Meta:
        model = Products
        fields = [
            "id",
            "category",
            "category_name",
            "title",
            "title_EN",
            "title_KY",
            "description",
            "description_EN",
            "description_KY",
            "composition",
            "composition_EN",
            "composition_KY",
            "image",
            "date",
            "price",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "name",
            "name_EN",
            "name_KY",
            "criteria_image",
            "text",
            "text_EN",
            "text_KY",
        ]
