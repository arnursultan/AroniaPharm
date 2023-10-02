from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.application.models import Application


class ApplicationViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.application_data = {
            "name": "Barry Allen",
            "mail": "grantgustin@gmail.com",
            "message": "This is a test application.",
        }
        self.application = Application.objects.create(**self.application_data)

    def test_create_application(self):
        url = reverse("application-list")
        response = self.client.post(url, self.application_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 2)

    def test_retrieve_application(self):
        url = reverse("application-detail", kwargs={"id": self.application.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.application_data["name"])

    def test_update_application(self):
        updated_data = {
            "name": "Updated Name",
            "mail": "updated@gmail.com",
            "message": "Updated application.",
        }
        url = reverse("application-detail", kwargs={"id": self.application.id})
        response = self.client.put(url, updated_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.application.refresh_from_db()
        self.assertEqual(self.application.name, updated_data["name"])

    def test_delete_application(self):
        url = reverse("application-detail", kwargs={"id": self.application.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Application.objects.count(), 0)
