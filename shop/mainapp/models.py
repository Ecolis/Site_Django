from django.db import models


class Category(models.Modal):
    name = models.CharField(
        max_length=255, verbose_name='Имя категории', db_index=True)
    # есть путь catigories\notebook - последнее это slag
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE)  # на случай удаления файла
    title = models.CharField(
        max_length=255, verbose_name='Наименование', db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(
        verbose_name='Изображение')  # изображение продукта
    # описание продукта, null - может быть пустым описание
    description = models.TextField(verbose_name='Описание', null='True')
    # maxdifits - максимальнаяя цена товара, decimal_places- количество знаков после запятой
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Стоимость')

    def __str__(self):
        return self.title


class Cartproduct(models.Model):
    user = models.ForeignKey(
        'Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    basket = models.ForeignKey(
        'Basket', verbose_name='Корзина', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Итог')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey(
        'Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(Cartproduct, blank=True)
    # в корзине у пользователя лежит телефон один и тот же 3 штуки и 2 телевизора один и тот же. По факту, продуктов всего 2,а количество их регулирует пользователь
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Итог')

    def __str__(self):
        return str(self.id)
