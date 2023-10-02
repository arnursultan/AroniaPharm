import os
from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from apps.products.models import Products, Review, Category
from apps.products.views import (
    ProductsListViewSet,
    CategoryListViewSet,
    ReviewListCreateView,
    ReviewViewSet,
)
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


class ViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.category = Category.objects.create(name="Test Category")

        test_image = self.create_test_image(name="test_image.jpg")

        self.product = Products.objects.create(
            category=self.category,
            title="Test Product",
            description="Test Description",
            composition="Test Composition",
            price="10.00",
            image=test_image,
        )

        criteria_image_name = self.create_test_criteria_image(
            name="test_criteria_image.jpg"
        )

        self.review = Review.objects.create(
            name="Test Review",
            criteria_image=criteria_image_name,
            text="Test Review Text",
        )

        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def create_test_image(self, name="test_image.jpg"):
        image = Image.new("RGB", (100, 100))
        image_io = BytesIO()
        image.save(image_io, "JPEG")
        image_io.seek(0)

        image_path = os.path.join(settings.MEDIA_ROOT, name)
        with open(image_path, "wb") as f:
            f.write(image_io.getvalue())

        return SimpleUploadedFile(name, image_io.getvalue(), content_type="image/jpg")

    def create_test_criteria_image(self, name="test_criteria_image.jpg"):
        image = Image.new("RGB", (100, 100))
        image_io = BytesIO()
        image.save(image_io, "JPEG")
        image_io.seek(0)

        image_path = os.path.join(settings.MEDIA_ROOT, name)
        with open(image_path, "wb") as f:
            f.write(image_io.getvalue())

        return name

    def test_products_list_viewset(self):
        view = ProductsListViewSet.as_view({"get": "list"})
        request = self.factory.get("/products/")
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_category_list_viewset(self):
        view = CategoryListViewSet.as_view({"get": "list"})
        request = self.factory.get("/categories/")
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_review_list_create_view(self):
        view = ReviewListCreateView.as_view()
        request = self.factory.get("/reviews/")
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_review_viewset(self):
        view = ReviewViewSet.as_view({"get": "list"})
        request = self.factory.get("/reviews/")
        response = view(request)
        self.assertEqual(response.status_code, 200)
