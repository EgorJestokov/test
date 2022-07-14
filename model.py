from django.db import models


# универсальный класс Indicator для справочников - КАРТОЧКА
class Indicator(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Наименование'
    )
    formula = models.TextField(
        verbose_name="Формула"
    )
    is_constant = models.BooleanField(
        default=False,
        verbose_name="Константа"
    )
    period_start = models.DateField(
        verbose_name="Начальная дата"
    )
    period_end = models.DateField(
        verbose_name="Конечная дата"
    )
    calculated_value = models.FloatField(
        verbose_name="Вычисляемое значение"
    )
    expected_value = models.FloatField(
        verbose_name="Ожидаемое значение"
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return self.name


# объект для создания товара/услуги
class CreateItemMod(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Наименование'
    )
    TYPE = [
        ('SER', 'Услуга'),
        ('PR', 'Товар'),
    ]
    type = models.CharField(
        choices=TYPE,
        max_length=25,
        default='PR',
        verbose_name='Тип'
    )
    unit = models.CharField(
        max_length=40,
        verbose_name='Единицы измерения'
    )
    price = models.ForeignKey(
        'Price',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Цена'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Добавить товар/услугу',
        verbose_name_plural = 'Добавить товары/услуги'

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.FloatField(
        verbose_name='Цена'
    )

    def __str__(self):
        return self.price
