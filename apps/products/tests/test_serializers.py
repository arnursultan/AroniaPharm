from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO
from apps.products.models import Category, Products, Review
from apps.products.serializers import (
    CategorySerializer,
    ProductsSerializer,
    ReviewSerializer,
)


class SerializerTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            name_EN="Test Category (EN)",
            name_KY="Test Category (KY)",
        )

        image = Image.new("RGB", (100, 100))
        image_io = BytesIO()
        image.save(image_io, "JPEG")
        image_io.seek(0)
        image_file = SimpleUploadedFile(
            "test.jpg", image_io.read(), content_type="image/jpeg"
        )

        self.product = Products.objects.create(
            category=self.category,
            title="Test Product",
            title_EN="Test Product (EN)",
            title_KY="Test Product (KY)",
            description="Test Description",
            description_EN="Test Description (EN)",
            description_KY="Test Description (KY)",
            composition="Test Composition",
            composition_EN="Test Composition (EN)",
            composition_KY="Test Composition (KY)",
            price="10.00",
            image=image_file,
        )

        criteria_image = Image.new("RGB", (100, 100))
        criteria_image_io = BytesIO()
        criteria_image.save(criteria_image_io, "JPEG")
        criteria_image_io.seek(0)
        criteria_image_file = SimpleUploadedFile(
            "test_criteria_image.jpg",
            criteria_image_io.read(),
            content_type="image/jpeg",
        )

        self.review = Review.objects.create(
            name="Test Review",
            name_EN="Test Review (EN)",
            name_KY="Test Review (KY)",
            criteria_image=criteria_image_file,
            text="Test Review Text",
            text_EN="Test Review Text (EN)",
            text_KY="Test Review Text (KY)",
        )

    def test_category_serializer(self):
        serializer = CategorySerializer(self.category)
        expected_data = {
            "id": self.category.id,
            "name": "Test Category",
            "name_EN": "Test Category (EN)",
            "name_KY": "Test Category (KY)",
        }
        self.assertEqual(serializer.data, expected_data)

    def test_products_serializer(self):
        serializer = ProductsSerializer(self.product)
        expected_data = {
            "id": self.product.id,
            "category": self.category.id,
            "category_name": "Test Category",
            "title": "Test Product",
            "title_EN": "Test Product (EN)",
            "title_KY": "Test Product (KY)",
            "description": "Test Description",
            "description_EN": "Test Description (EN)",
            "description_KY": "Test Description (KY)",
            "composition": "Test Composition",
            "composition_EN": "Test Composition (EN)",
            "composition_KY": "Test Composition (KY)",
            "image": f'/media/products/{self.product.image.name.split("/")[-1]}',
            "date": self.product.date.strftime("%Y-%m-%d"),
            "price": "10.00",
        }
        self.assertEqual(serializer.data, expected_data)

    def test_review_serializer(self):
        serializer = ReviewSerializer(self.review)
        expected_data = {
            "id": self.review.id,
            "name": "Test Review",
            "name_EN": "Test Review (EN)",
            "name_KY": "Test Review (KY)",
            "criteria_image": f'/media/criteria_images/{self.review.criteria_image.name.split("/")[-1]}',
            "text": "Test Review Text",
            "text_EN": "Test Review Text (EN)",
            "text_KY": "Test Review Text (KY)",
        }
        self.assertEqual(serializer.data, expected_data)
