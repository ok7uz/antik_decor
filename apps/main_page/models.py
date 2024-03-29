import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Banner(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    image = models.ImageField('Изображение', upload_to='banner/')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField('Название', max_length=255)
    url = models.URLField('Ссылка на YouTube')
    banner = models.ImageField('Изображение для видео', upload_to='video-banner/')

    class Meta:
        ordering = ['-id']
        verbose_name = 'видео'
        verbose_name_plural = 'видео'

    def __str__(self):
        return self.title


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField('Название', max_length=255)
    content = RichTextUploadingField('Контент')
    image = models.ImageField('Изображение', upload_to='news/')
    date = models.DateField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
