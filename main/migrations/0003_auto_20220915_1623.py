# Generated by Django 3.1.7 on 2022-09-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220914_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name_plural': 'Order items'},
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Общая стоимость заказа'),
        ),
        migrations.AlterUniqueTogether(
            name='orderitems',
            unique_together={('item', 'order')},
        ),
        migrations.RemoveField(
            model_name='orderitems',
            name='discount',
        ),
    ]
