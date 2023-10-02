from googletrans import Translator

translator = Translator()


class ProductsService:
    @staticmethod
    def translate_products_service(products, lang):
        products.category.name = translator.translate(
            products.category.name, dest=lang
        ).text
        products.title = translator.translate(products.title, dest=lang).text
        products.description = translator.translate(
            products.description, dest=lang
        ).text
        products.composition = translator.translate(
            products.composition, dest=lang
        ).text

        return products


class CategoryService:
    @staticmethod
    def translate_category_service(category, lang):
        category.name = translator.translate(category.name, dest=lang).text

        return category


class ReviewService:
    @staticmethod
    def translate_review_service(review, lang):
        review.name = translator.translate(review.name, dest=lang).text
        review.text = translator.translate(review.text, dest=lang).text

        return review
