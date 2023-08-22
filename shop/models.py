from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='продукт')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    buy_cost = models.IntegerField(verbose_name='стоимость покупки')


    def __str__(self):
        return f'{self.product_name} {self.category} {self.buy_cost} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'