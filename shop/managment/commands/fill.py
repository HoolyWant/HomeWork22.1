from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        product_list = [
            {'product_name': 'Установка винды', 'description': 'Чистая установка',
             'category_name': 'Услуга', 'buy_cost': '500'},
            {'product_name': 'Ктото', 'description': 'Мы ему не доверяем',
             'category_name': '4', 'buy_cost': '43545'},
            {'product_name': 'Непонятное', 'description': 'Не понимаем такое',
             'category_name': '2', 'buy_cost': '5009'},
            {'product_name': 'Какоето', 'description': 'СТранное оно',
             'category_name': '2', 'buy_cost': '399'},
            {'product_name': 'Незнамашо', 'description': 'Ну тут не прибавить не отбавить',
             'category_name': '3', 'buy_cost': '10'},
            {'product_name': 'Невиданное', 'description': 'Не видали раньше',
             'category_name': '4', 'buy_cost': '1234000'},
        ]
        products_for_create = []
        for category in product_list:
            products_for_create.append(
                Product(**category)
            )

        Product.objects.bulk_create(products_for_create)
