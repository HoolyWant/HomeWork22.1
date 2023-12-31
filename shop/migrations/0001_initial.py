# Generated by Django 4.2.4 on 2023-08-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='контент')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('activity_sign', models.BooleanField(verbose_name='активна')),
                ('view_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='продукт')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение')),
                ('category', models.CharField(blank=True, max_length=150, null=True, verbose_name='описание')),
                ('buy_cost', models.IntegerField(verbose_name='стоимость покупки')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
