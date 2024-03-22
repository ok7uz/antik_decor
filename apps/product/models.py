from django.db import models

from apps.product.managers import SubCategoryManager, CategoryManager, NewProductsManager


class BaseCategory(models.Model):
    name = models.CharField('Название', max_length=128)
    parent = models.ForeignKey('self', verbose_name='Высшая категория', on_delete=models.CASCADE,
                               related_name='sub_categories', null=True)
    image = models.ImageField('Изображение', upload_to='category/', null=True)
    is_top = models.BooleanField('Верхнее меню?', default=False)
    is_left = models.BooleanField('Левое меню?', default=False)

    objects = models.Manager()

    class Meta:
        ordering = ['-is_top', 'parent__id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        str_name = self.name
        parent = self.parent

        while parent:
            str_name = f'{parent.name} / ' + str_name
            parent = parent.parent

        return str_name


class Category(BaseCategory):
    objects = CategoryManager()

    class Meta:
        proxy = True
        ordering = ['-is_top', 'id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(BaseCategory):
    objects = SubCategoryManager()

    class Meta:
        proxy = True
        ordering = ['-parent__is_top', '-parent', 'name']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    name = models.CharField('Название продукта', max_length=255, unique=False,)
    category = models.ManyToManyField(BaseCategory, verbose_name='Категории', related_name='products')
    description = models.TextField('Описание')

    price = models.PositiveIntegerField('Цена',)
    is_new = models.BooleanField('Новый?', default=False)
    created = models.DateField('Дата создания', auto_now_add=True)
    vendor_code = models.CharField('Артикул', max_length=32)
    history = models.CharField('История', max_length=255)
    characteristic = models.CharField('Характеристики', max_length=255)
    size = models.CharField('Размер', max_length=255)
    video_url = models.URLField('Ссылка на видео о продукте на YouTube', blank=True, null=True)

    objects = models.Manager()
    new_products = NewProductsManager()

    class Meta:
        ordering = ['-created', 'name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return "product/{}-{}.jpg".format(instance.product.id, instance.product.images.count() + 1)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='images')
    image = models.ImageField(upload_to=upload_to, null=True, blank=True, default=None)

    objects = models.Manager()

    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'

    def __str__(self):
        return self.image.url
