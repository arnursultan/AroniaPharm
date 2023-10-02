from django.db import models
from PIL import Image
from .utils import (
    save_photo_with_resized_image,
    save_certificate_with_resized_image,
    save_logo_with_resized_image,
)


class Photo(models.Model):
    image = models.ImageField(
        upload_to="",
        default="default_photo.jpg",
        verbose_name="Фотография"
    )
    caption = models.CharField(
        max_length=100,
        default="Main Photo",
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.caption or str(self.pk)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        save_photo_with_resized_image(self)


class Certificate(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="certificates/",
        db_index=False,
        verbose_name="Фотография сертификата"
    )

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return f"Certificate {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        save_certificate_with_resized_image(self)


class Logo(models.Model):
    image = models.ImageField(
        upload_to="photos/",
        verbose_name="Фотография"
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата загрузки"
    )

    class Meta:
        verbose_name = "Партнера"
        verbose_name_plural = "Наши партнеры"

    def __str__(self):
        return f"Logo {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        save_logo_with_resized_image(self)


class Video(models.Model):
    video_code = models.CharField(
        max_length=20,
        verbose_name="Код видеоролика"
    )

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.video_code
