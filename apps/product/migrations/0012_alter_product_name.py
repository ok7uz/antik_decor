# Generated by Django 5.0.3 on 2024-03-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_basecategory_left_menu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название продукта'),
        ),
    ]