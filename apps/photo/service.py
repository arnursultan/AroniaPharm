from googletrans import Translator

translator = Translator()


def translate_instance_service(instance, lang):
    instance.title = translator.translate(instance.title, dest=lang).text
    instance.description = translator.translate(instance.description, dest=lang).text
    return instance
