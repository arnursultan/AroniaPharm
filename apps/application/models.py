from django.db import models


class Application(models.Model):
    name = models.CharField(
        max_length=127,
        verbose_name="Имя"
    )
    mail = models.EmailField(
        blank=True, null=True,
        verbose_name="Email"
    )
    message = models.TextField(
        max_length=255,
        verbose_name="Сообщение"
    )
    date = models.DateField(
        auto_now=True
    )
    considered = models.BooleanField(
        default=False,
        verbose_name="Рассмотрена"
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.name
