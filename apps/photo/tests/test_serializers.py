from django.test import TestCase
from apps.photo.models import Photo, Certificate, Logo, Video
from apps.photo.serializers import (
    PhotoSerializer,
    CertificateSerializer,
    LogoSerializer,
    VideoSerializer,
)
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO


class PhotoSerializerTestCase(TestCase):
    def setUp(self):
        image = Image.new("RGB", (100, 100))
        image_data = BytesIO()
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )

        self.photo_data = {"image": image_file, "caption": "Test Caption"}
        self.serializer = PhotoSerializer(data=self.photo_data)

    def _test_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data, self.photo_data)

    def test_valid_serializer(self):
        self._test_serializer()

    def test_serialized_data(self):
        self._test_serializer()


class CertificateSerializerTestCase(TestCase):
    def setUp(self):
        image = Image.new("RGB", (100, 100))
        image_data = BytesIO()
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )

        self.certificate_data = {
            "title": "Test Certificate",
            "title_EN": "Test Certificate EN",
            "title_KY": "Test Certificate KY",
            "description": "Test Description",
            "description_EN": "Test Description EN",
            "description_KY": "Test Description KY",
            "image": image_file,
        }
        self.serializer = CertificateSerializer(data=self.certificate_data)

    def _test_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data, self.certificate_data)

    def test_valid_serializer(self):
        self._test_serializer()

    def test_serialized_data(self):
        self._test_serializer()


class LogoSerializerTestCase(TestCase):
    def setUp(self):
        image = Image.new("RGB", (100, 100))
        image_data = BytesIO()
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )

        self.logo_data = {"image": image_file}
        self.serializer = LogoSerializer(data=self.logo_data)

    def _test_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data, self.logo_data)

    def test_valid_serializer(self):
        self._test_serializer()

    def test_serialized_data(self):
        self._test_serializer()

class VideoSerializerTestCase(TestCase):
    def setUp(self):
        self.video_data = {"video_code": "ABC123"}
        self.serializer = VideoSerializer(data=self.video_data)

    def _test_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data, self.video_data)

    def test_valid_serializer(self):
        self._test_serializer()

    def test_serialized_data(self):
        self._test_serializer()