from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "mail", "message", "date", "get_consideration_status")
    list_filter = ("name", "mail", "considered")
    date_hierarchy = "date"

    def get_consideration_status(self, obj):
        if obj.considered:
            return "Рассмотрена"
        else:
            return "Не рассмотрена"

    get_consideration_status.short_description = "Статус заявки"
