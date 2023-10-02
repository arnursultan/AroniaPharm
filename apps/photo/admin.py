from django.contrib import admin
from .models import Photo, Certificate, Logo, Video


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "caption")
    list_filter = (
        "id",
        "caption",
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    fields = (
        "image",
        "title",
        "title_EN",
        "title_KY",
        "description",
        "description_EN",
        "description_KY",
    )
    list_filter = (
        "id",
        "title",
        "description",
    )
    list_display_links = ("title",)


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "uploaded_at")
    list_filter = (
        "id",
        "uploaded_at",
    )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video_code")
    list_display_links = ("video_code",)
