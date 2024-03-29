# Generated by Django 5.0.3 on 2024-03-27 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, verbose_name='Имя клиента')),
                ('customer_phone', models.CharField(max_length=20, verbose_name='Телефон клиента')),
                ('customer_email', models.EmailField(max_length=254, verbose_name='Email клиента')),
                ('customer_address', models.TextField(verbose_name='Адрес клиента')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('processing', 'В обработке'), ('shipped', 'Отправлено'), ('delivered', 'Доставлено'), ('cancelled', 'Отменено')], default='pending', max_length=32, verbose_name='Статус')),
                ('total_price', models.PositiveIntegerField(verbose_name='Сумма заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order', verbose_name='Заказы')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='product.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиции заказов',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', through='order.OrderItem', to='product.product'),
        ),
    ]
