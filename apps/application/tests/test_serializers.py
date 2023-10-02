from django.test import TestCase
from apps.application.models import Application
from apps.application.serializers import ApplicationSerializer


class ApplicationSerializerTestCase(TestCase):
    def test_serializer_with_valid_data(self):
        valid_data = {
            "name": "Grant Gustin",
            "mail": "theflash@gmail.com",
            "message": "Test message",
        }

        serializer = ApplicationSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        serialized_data = serializer.data
        self.assertEqual(serialized_data, valid_data)

    def test_serializer_with_invalid_data(self):
        invalid_data = {
            "id": 1,
            "name": "Grant Gustin",
            "mail": "invalid_email",
            "message": "Test message",
        }

        serializer = ApplicationSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_create(self):
        valid_data = {
            "id": 1,
            "name": "Grant Gustin",
            "mail": "theflash@gmail.com",
            "message": "Test message",
        }

        serializer = ApplicationSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()

        self.assertEqual(instance.name, "Grant Gustin")
        self.assertEqual(instance.mail, "theflash@gmail.com")
        self.assertEqual(instance.message, "Test message")

    def test_serializer_update(self):
        application = Application.objects.create(
            name="Initial Name", mail="initial@gmail.com", message="Initial message"
        )

        updated_data = {
            "id": application.id,
            "name": "Updated Name",
            "mail": "updated@gmail.com",
            "message": "Updated message",
        }

        serializer = ApplicationSerializer(
            instance=application, data=updated_data, partial=True
        )
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()

        self.assertEqual(updated_instance.name, "Updated Name")
        self.assertEqual(updated_instance.mail, "updated@gmail.com")
        self.assertEqual(updated_instance.message, "Updated message")
