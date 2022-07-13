from django.db import models


# универсальный класс Indicator для справочников
class Indicator(models.Model):
    name = models.CharField(max_length=70)
    formula = models.TextField
    is_constant = models.BooleanField(default=False)
    period = models.DateTimeField
    calculated_value = models.FloatField
    expected_value = models.FloatField

    class Meta:
        ordering = ['name']
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'

    def __str__(self):
        return self.name


class Price(models.Model):
    price_lower = models.DecimalField(decimal_places=2, max_digits=10)
    price_upper = models.DecimalField(decimal_places=2, max_digits=10)


# кнопка создать в справочнике
class CreateMod(models.Model):
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=50)
    unit = models.CharField(max_length=40)
    price = models.OneToOneField(Price, on_delete=models.CASCADE, primary_key=True)


# Справочник цен
class Price_manual(models.Model):
    name = models.OneToOneField(CreateMod, on_delete=models.CASCADE, primary_key=True)  # Наследование класса
    type = models.CharField(max_length=50)  # сделать переключатель
    period = models.DateTimeField
    real_Price = models.DecimalField(decimal_places=2, max_digits=10)
    rate_NDS = models.DecimalField(decimal_places=2, max_digits=10)  # выпадающий список с  0% 10% 20%
    NDS = models.FloatField
    NDS_price = models.FloatField

    # +кнопка сохранить и кнопка отменить

    def NDS(self):
        return self.real_Price * self.rate_NDS

    def NDS_price(self):
        return self.real_Price * self.NDS

    # def Validator:


# Справочник объемов продаж
class Value_sales(models.Model):
    name = models.OneToOneField(CreateMod, on_delete=models.CASCADE, primary_key=True)  # Наследование класса
    type = models.CharField(max_length=50)  # сделать переключатель
    period = models.DateTimeField
    unit = models.CharField(max_length=40)  # Наследование класса
    value_nat = models.IntegerField  # ?? что значит нат. единиц
    # +кнопка сохранить и кнопка отменить

    #def __init__(self, ):








# class Period:
#     type
#     start_point
#     end_point
#
# class Period_point:
#     date