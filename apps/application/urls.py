from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationDetailViewSet, ApplicationListViewSet

router = DefaultRouter()
router.register("applications", ApplicationListViewSet)
router.register("applications", ApplicationDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
