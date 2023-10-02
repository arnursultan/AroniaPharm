from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO
from apps.products.models import Category, Products, Review


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_category_name(self):
        self.assertEqual(str(self.category), "Test Category")


class ProductsModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        image = Image.new("RGB", (100, 100))
        image_io = BytesIO()
        image.save(image_io, format="JPEG")
        image_io.seek(0)
        self.image_file = SimpleUploadedFile("test_image.jpg", image_io.read())

        self.product = Products.objects.create(
            image=self.image_file,
            category=self.category,
            title="Test Product",
            description="Test Description",
            composition="Test Composition",
            price=10.00,
        )

    def test_product_title(self):
        self.assertEqual(str(self.product), "Test Product")

    def test_product_image_thumbnail(self):
        img = Image.open(self.product.image.path)
        self.assertEqual(img.width, 50)
        self.assertEqual(img.height, 50)


class ReviewModelTestCase(TestCase):
    def setUp(self):
        image = Image.new("RGB", (100, 100))
        image_io = BytesIO()
        image.save(image_io, format="JPEG")
        image_io.seek(0)
        self.image_file = SimpleUploadedFile("test_image.jpg", image_io.read())

        self.review = Review.objects.create(
            name="Test Review",
            criteria_image=self.image_file,
            text="Test Review Text",
        )

    def test_review_name(self):
        expected_name = "Test Review"
        self.assertEqual(str(self.review), expected_name)

    def test_review_image_thumbnail(self):
        img = Image.open(self.review.criteria_image.path)
        self.assertEqual(img.width, 50)
        self.assertEqual(img.height, 50)
