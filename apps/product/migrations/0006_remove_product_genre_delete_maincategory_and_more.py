# Generated by Django 5.0.3 on 2024-03-19 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_genre_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='genre',
        ),
        migrations.DeleteModel(
            name='MainCategory',
        ),
        migrations.AlterModelOptions(
            name='basecategory',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='authorship',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]