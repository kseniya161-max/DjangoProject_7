from django.db import models


class Category(models.Model):
    """ Модель Категории Продуктов
    """
    name = models.CharField(max_length=50, verbose_name='Категория продукта')
    photo = models.ImageField(upload_to='photo/category/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_manage_category", "Can manage category"),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель Продуктов"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Наименование продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    quantity = models.IntegerField(verbose_name='Количество')
    photo = models.ImageField(upload_to='photo/product/', blank=True, null=True, verbose_name='фото')
    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_manage_product", "Can manage product"),
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'