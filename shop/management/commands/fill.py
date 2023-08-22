from django.core.management import BaseCommand
from shop.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Product.objects.all().delete()
        Product.truncate_table_restart_id()
        product_list = [
            {'product_name': 'Установка винды', 'description': 'Чистая установка',
             'category': 'Услуга', 'buy_cost': '500'},
            {'product_name': 'Развод мостов', 'description': 'По расписанию',
             'category': 'Услуга', 'buy_cost': '100500'},
            {'product_name': 'Баралгин', 'description': 'Лечит от всего',
             'category': 'Лекарство', 'buy_cost': '140'},
            {'product_name': 'Автомобиль', 'description': 'Без документов, черная продажа',
             'category': 'Средство передвижения', 'buy_cost': '1000'},
            {'product_name': 'Пришивание рукава', 'description': 'Бесполезная вещь',
             'category': 'Мед. услуга', 'buy_cost': '10'},
        ]
        products_for_create = []
        for category in product_list:
            products_for_create.append(
                Product(**category)
            )

        Product.objects.bulk_create(products_for_create)
