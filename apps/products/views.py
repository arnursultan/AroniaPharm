from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, mixins, generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Products, Review, Category
from .serializers import ProductsSerializer, ReviewSerializer, CategorySerializer
from googletrans import Translator

translator = Translator()

from .service import ProductsService
from .service import CategoryService
from .service import ReviewService


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get("lang", "ru")


class ProductsListViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance = ProductsService.translate_products_service(instance, lang)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryListViewSet(
    LanguageParamMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance = CategoryService.translate_category_service(instance, lang)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ReviewListCreateView(LanguageParamMixin, generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]

class ReviewViewSet(LanguageParamMixin, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance = ReviewService.translate_review_service(instance, lang)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
