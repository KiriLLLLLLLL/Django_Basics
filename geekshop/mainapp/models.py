from django.db import models


class CategoryMenu(models.Model):

    name = models.CharField(
        verbose_name='имя',
        max_length=64,
    )

    href = models.CharField(
        verbose_name='ссылка',
        max_length=64,
        default='#',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'меню категории'
        verbose_name_plural = 'меню категорий'

class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )

    category_menu = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE,
        verbose_name='категория меню',
    )

    name = models.CharField(
        verbose_name='имя',
        max_length=128,
    )

    short_desc = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='краткое описание',
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )

    def __str__(self):
        return f'{self.name} - {self.id}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

