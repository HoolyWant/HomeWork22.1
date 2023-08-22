from django.db import models, connection

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='продукт')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    buy_cost = models.IntegerField(verbose_name='стоимость покупки')

    def __str__(self):
        return f'{self.product_name}'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'