from PIL import Image


def save_products_with_resized_image(instance):
    if instance.image:
        img = Image.open(instance.image.path)
        desired_size = (img.width // 2, img.height // 2)
        img.thumbnail(desired_size)
        img.save(instance.image.path)


def save_review_with_resized_image(instance):
    if instance.criteria_image:
        img = Image.open(instance.criteria_image.path)
        desired_size = (img.width // 2, img.height // 2)
        img.thumbnail(desired_size)
        img.save(instance.criteria_image.path)
