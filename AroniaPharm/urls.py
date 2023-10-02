from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.application.urls import router as application_router
from apps.products.urls import router as products_router
from apps.photo.urls import router as photo_router
from rest_framework.routers import DefaultRouter
from .settings.yasg import urlpatterns_swagger
from apps.products.catalog import DownloadProductsXLS


router = DefaultRouter()
router.registry.extend(application_router.registry)
router.registry.extend(products_router.registry)
router.registry.extend(photo_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "download/products-xls/",
        DownloadProductsXLS.as_view(),
        name="download-products-xls",
    ),
]

urlpatterns += urlpatterns_swagger

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
