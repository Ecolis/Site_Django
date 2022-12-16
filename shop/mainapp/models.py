from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class Category(models.Modal):
    name = models.CharField(
        max_length=255, verbose_name='Имя категории', db_index=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255, verbose_name='Наименование', db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null='True')
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Стоимость')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey(
        'Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey(
        'Cart', verbose_name='Корзина', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Итог')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)


class Dress(Product):
    style = models.CharField(max_length=255, verbose_name='Фасон')
    structure = models.CharField(max_length=255, verbose_name='Состав')
    cut = models.CharField(max_length=255, verbose_name='Крой')
    silhouette = models.CharField(max_length=255, verbose_name='Силуэт')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    length = models.CharField(max_length=255, verbose_name='Длина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class skirt(Product):
    style = models.CharField(max_length=255, verbose_name='Фасон')
    structure = models.CharField(max_length=255, verbose_name='Состав')
    cut = models.CharField(max_length=255, verbose_name='Крой')
    silhouette = models.CharField(max_length=255, verbose_name='Силуэт')
    landing = models.CharField(max_length=255, verbose_name='Посадка')
    length = models.CharField(max_length=255, verbose_name='Длина')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Cart(models.Model):
    owner = models.ForeignKey(
        'Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        CartProduct, blank=True, related_name='related_card')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Итог')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    numberphone = models.CharField(
        max_length=20, verbose_name='Номер телефона')
    adress = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return 'Покупатель: {} {}'.format(self.user.first_name, self.user.last_name)

