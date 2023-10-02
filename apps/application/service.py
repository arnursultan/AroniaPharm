from django.core.mail import send_mail


def create_application_service(instance):
    subject = "Новая заявка"
    message = f"Клиент с именем {instance.name} подал заявку под номером {instance.id}"
    from_email = ""
    recipient_list = [""]

    send_mail(subject, message, from_email, recipient_list)
