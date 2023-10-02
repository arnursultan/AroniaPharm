from django.test import TestCase
from apps.application.models import Application


class ApplicationModelTestCase(TestCase):
    def test_create_application(self):
        application = Application.objects.create(
            name="Grant Gustin",
            mail="theflash@gmail.com",
            message="Test message",
            considered=True,
        )

        self.assertEqual(application.name, "Grant Gustin")
        self.assertEqual(application.mail, "theflash@gmail.com")
        self.assertEqual(application.message, "Test message")
        self.assertEqual(application.considered, True)

    def test_default_values(self):
        application = Application.objects.create(name="Iris")

        self.assertEqual(application.mail, None)
        self.assertEqual(application.considered, False)

    def test_str_representation(self):
        application = Application.objects.create(name="Joe")

        self.assertEqual(str(application), "Joe")
