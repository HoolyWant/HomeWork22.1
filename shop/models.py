from django.db import models, connection

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='продукт')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='категория', **NULLABLE)
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


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='контент')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    activity_sign = models.BooleanField(verbose_name='активна')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_title = models.CharField(max_length=100, verbose_name='название версии')
    version_number = models.IntegerField(verbose_name='номер версии')
    is_active = models.BooleanField(verbose_name='активна')

    def __str__(self):
        return f'{self.version_title} {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

