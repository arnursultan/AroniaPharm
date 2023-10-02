from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.photo.models import Photo, Certificate, Logo, Video
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO


class CertificateViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        image = Image.new("RGB", (100, 100))
        image_data = BytesIO()
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )
        self.certificate_data = {
            "title": "Test Certificate",
            "description": "Test Description",
            "image": image_file,
        }
        self.certificate = Certificate.objects.create(**self.certificate_data)

    def test_retrieve_certificate_translation(self):
        response = self.client.get(f"/api/certificates/{self.certificate.id}/?lang=en")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Certificate")


class LogoCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_logo(self):
        image = Image.new("RGB", (100, 100))
        image_data = BytesIO()
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )

        response = self.client.post(
            "/api/logos/",
            {
                "image": image_file,
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Logo.objects.count(), 1)


class VideoViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.video_data = {"video_code": "ABC123"}
        self.video = Video.objects.create(**self.video_data)

    def test_list_videos(self):
        response = self.client.get("/api/videos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class PhotoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_photo(self):
        image = Image.new("RGB", (100, 100))
        image_data = BytesIO()
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )

        response = self.client.post(
            "/api/photos/",
            {
                "image": image_file,
                "caption": "Test Photo Caption",
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Photo.objects.count(), 1)

    def test_photo_str_method(self):
        image = Image.new("RGB", (100, 100))
        image_data = BytesIO()
        image.save(image_data, "PNG")
        image_data.seek(0)
        image_file = SimpleUploadedFile(
            "test_image.png", image_data.read(), content_type="image/png"
        )

        photo = Photo.objects.create(image=image_file, caption="Test Caption")
        self.assertEqual(str(photo), "Test Caption")
