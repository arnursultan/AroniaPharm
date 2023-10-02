from django.db import models
from PIL import Image
from .utils import save_products_with_resized_image, save_review_with_resized_image


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    image = models.ImageField(
        upload_to="products",
        blank=True,
        verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    title = models.CharField(
        max_length=127,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    composition = models.TextField(
        verbose_name="Состав"
    )
    date = models.DateField(
        auto_now=True,
        verbose_name="Дата"
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        save_products_with_resized_image(self)


class Review(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    criteria_image = models.ImageField(
        upload_to="criteria_images/",
        verbose_name="Изображение"
    )
    text = models.CharField(
        max_length=500,
        verbose_name="Текст"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        save_review_with_resized_image(self)
