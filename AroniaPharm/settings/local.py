from .base import *
from .development import *


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    # ""
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    # ""
]

CORS_ALLOW_HEADERS = (
    'content-type', 'accept', 'origin', 'Authorization'
)

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"] + CORS_ALLOWED_ORIGINS

# CSRF_TRUSTED_ORIGINS = [""]
