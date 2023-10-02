from PIL import Image


def save_photo_with_resized_image(instance):
    if instance.image:
        img = Image.open(instance.image.path)
        desired_size = (img.width // 2, img.height // 2)
        img.thumbnail(desired_size)
        img.save(instance.image.path)


def save_certificate_with_resized_image(instance):
    if instance.image:
        img = Image.open(instance.image.path)
        desired_size = (img.width // 2, img.height // 2)
        img.thumbnail(desired_size)
        img.save(instance.image.path)


def save_logo_with_resized_image(instance):
    if instance.image:
        img = Image.open(instance.image.path)
        desired_size = (img.width // 2, img.height // 2)
        img.thumbnail(desired_size)
        img.save(instance.image.path)
