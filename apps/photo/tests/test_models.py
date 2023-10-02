from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.photo.models import Photo, Certificate, Logo, Video
from PIL import Image
from io import BytesIO


class PhotoModelTestCase(TestCase):
    def setUp(self):
        image_data = BytesIO()
        image = Image.new("RGB", (100, 100))
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )

        self.photo = Photo.objects.create(image=image_file, caption="Test Photo")

    def test_photo_str(self):
        self.assertEqual(str(self.photo), "Test Photo")


class CertificateModelTestCase(TestCase):
    def setUp(self):
        # Create a test image file
        image_data = BytesIO()
        image = Image.new("RGB", (100, 100))
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_certificate.png", image_data.read(), content_type="image/png"
        )

        self.certificate = Certificate.objects.create(
            image=image_file, title="Test Certificate", description="Test Description"
        )

    def test_certificate_str(self):
        self.assertEqual(str(self.certificate), "Certificate 1")


class LogoModelTestCase(TestCase):
    def setUp(self):
        # Create a test image file
        image_data = BytesIO()
        image = Image.new("RGB", (100, 100))
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_logo.png", image_data.read(), content_type="image/png"
        )

        self.logo = Logo.objects.create(image=image_file)

    def test_logo_str(self):
        self.assertEqual(str(self.logo), "Logo 1")


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.video = Video.objects.create(video_code="ABC123")

    def test_video_str(self):
        self.assertEqual(str(self.video), "ABC123")
