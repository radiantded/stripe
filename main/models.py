from django.db import models


class Item(models.Model):
    name = models.CharField(
        verbose_name='Название товара',
        max_length=50
    )
    description = models.CharField(
        verbose_name='Описание товара',
        max_length=200
    )
    price = models.DecimalField(
        verbose_name='Цена товара',
        decimal_places=2,
        max_digits=10
    )

    def __str__(self) -> str:
        return f'{self.name}: {self.price}'


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        related_name='order',
        through='OrderItems'
    )
    creation_time = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    comment = models.CharField(
        verbose_name='Комментарий',
        max_length=1000,
        null=True,
        blank=True
    )
    cost = models.DecimalField(
        verbose_name='Общая стоимость заказа',
        decimal_places=2,
        max_digits=10,
        null=True,
        blank=True
    )
    discount = models.DecimalField(
        verbose_name='Скидка',
        max_digits=3,
        decimal_places=0,
        default=0
    )

    def __str__(self) -> str:
        return f'ID: {self.id}'

    def get_cost(self):
        cost = 0
        for item in self.items.all():
            cost += item.price
        cost_with_discount = cost - cost * (self.discount / 100)
        self.cost = cost_with_discount
        return self.cost


class OrderItems(models.Model):
    item = models.ForeignKey(
        Item,
        verbose_name='Товар',
        on_delete=models.PROTECT,
        null=True
    )
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = [['item', 'order']]
        verbose_name_plural = 'Order items'
