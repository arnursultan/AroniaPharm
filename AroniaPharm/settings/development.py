import os
from .base import *

# General Settings
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")

# Application definition
CREATE_APPS = [
    "apps.products",
    "apps.application",
    "apps.photo",
]
INSTALLED_LIBRARY = [
    "jazzmin",
    "drf_yasg",
    "django_filters",
    "modeltranslation",
    "rest_framework",
    "corsheaders",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS
