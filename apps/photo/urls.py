from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet, CertificateViewSet, LogoCreateView, VideoViewSet

router = DefaultRouter()
router.register(r"photos", PhotoViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"logos", LogoCreateView, basename="logo")
router.register(r"videos", VideoViewSet)

urlpatterns = router.urls
