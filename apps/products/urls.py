from rest_framework.routers import DefaultRouter
from .views import ProductsListViewSet, ReviewViewSet, CategoryListViewSet

router = DefaultRouter()
router.register("products", ProductsListViewSet)
router.register("review", ReviewViewSet)
router.register("category", CategoryListViewSet)

urlpatterns = router.urls
