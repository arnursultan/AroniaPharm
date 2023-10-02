from modeltranslation.translator import register, TranslationOptions
from .models import Certificate


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ("title", "description")
