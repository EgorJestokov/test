from django.db import models

class Type_n_Unit(models.Model):
    type = models.CharField(null=False,blank=False,default='',choices=(('Продукт','Продукт'),('Услуга','Услуга')),max_length=25,verbose_name='Тип')
    unit = models.CharField(null=False,blank=False,default='',choices=(('Услуга','-'),('Кг','КГ'),('Гр','Г'),('Шт','ШТ'),('Л','Л'),('Упаковка','УПАК')),max_length=40,verbose_name='Единицы измерения')

    class Meta:
        abstract = True


class Type(models.Model):
    type = models.CharField(null=False,blank=False,default='',choices=(('Продукт','Продукт'),('Услуга','Услуга')),max_length=25,verbose_name='Тип')

    class Meta:
        abstract = True


class Unit(models.Model):
    unit = models.CharField(null=False,blank=False,default='',choices=(('Услуга','-'),('Кг','КГ'),('Гр','Г'),('Шт','ШТ'),('Л','Л'),('Упаковка','УПАК')),max_length=40,verbose_name='Единицы измерения')

    class Meta:
        abstract = True


#универсальный класс Indicator для справочников - КАРТОЧКА
class Indicator(models.Model):
    title = models.CharField(max_length=70,verbose_name='Наименование')
    date = models.DateTimeField(verbose_name='Дата')
    formula = models.TextField(verbose_name="Формула")
    is_constant = models.BooleanField(default=False,verbose_name="Константа")
    period_start = models.DateField(verbose_name="Начальная дата")
    period_end = models.DateField(verbose_name="Конечная дата")
    calculated_value = models.FloatField(verbose_name="Вычисляемое значение")
    expected_value = models.FloatField(verbose_name="Ожидаемое значение")

    class Meta:
        ordering = ['title']
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return self.title

# объект для создания товара/услуги
class CreateProduct(Type_n_Unit):
    name = models.CharField(max_length=70,verbose_name='Наименование')
    # typeProduct = models.ForeignKey('Type',on_delete=models.CASCADE, related_name='choice_of_Types_Prod')
    # typeProduct = models.ForeignKey('Type',on_delete=models.CASCADE, verbose_name='Тип')
    quantity = models.IntegerField(verbose_name='Количество',default=0)
    # unitProduct = models.ForeignKey('Unit',on_delete=models.CASCADE, related_name='choice_of_Units_Prod')
    # unitProduct = models.ForeignKey('Unit',on_delete=models.CASCADE, verbose_name='Единицы измерения')
    date = models.DateTimeField(blank=True, null=True, auto_now=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Добавить товар/услугу',
        verbose_name_plural = 'Добавить товары/услуги'

    def __str__(self):
        return self.name


# объект для справочника цен
class CreatePrice(Type):
    # typePrice = models.ForeignKey('Type',on_delete=models.CASCADE, related_name='choice_of_Types_Price')
    # typePrice = models.ForeignKey('Type',on_delete=models.CASCADE, verbose_name='Тип')
    date = models.DateTimeField(verbose_name='Дата')
    period_type = models.CharField(default="День", max_length=10, choices=(('День', 'День'),('Месяц', 'Месяц'),('Квартал', 'Квартал'),('Год', 'Год')), verbose_name='Тип временного периода')
    period_start = models.DateField(verbose_name='Начало периода')
    period_end = models.DateField(verbose_name='Конец периода')
    price_non_nds = models.IntegerField(verbose_name='Цена без НДС', default=0)
    NDS_type = models.IntegerField(default="0",choices=((0,'0'),(10,'10'),(20,'20')), verbose_name='Тип НДС')
    NDS = models.FloatField(verbose_name='НДС', default=0)
    price_with_nds = models.FloatField(verbose_name='Цена с НДС', default=0)

    class Meta():
        ordering = ['-date']
        verbose_name='Создать цену'
        verbose_name_plural='Создать цены'

    def __str__(self):
        return self.type


class CreateSale(Type_n_Unit):
    # typeSale = models.ForeignKey('Type',on_delete=models.CASCADE, related_name='choice_of_Types_Sale')
    # typeSale = models.ForeignKey('Type',on_delete=models.CASCADE, verbose_name='Тип')
    period_type = models.CharField(default="День",max_length=10,choices=(('day', 'День'),('month', 'Месяц'),('quarter', 'Квартал'),('year', 'Год')), verbose_name='Тип временного периода')
    period_start = models.DateField(verbose_name='Начало временного периода')
    period_end = models.DateField(verbose_name='Конец временного периода')
    # unitSale = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='choice_of_Units_Sale', verbose_name='Единицы измерения')
    value_nat = models.FloatField(max_length=10,default='',verbose_name='Значение')


    class Meta:
        verbose_name='Создать объём продаж'
        verbose_name_plural='Создать объемы продаж'

    def __str__(self):
        return self.type

class CreateManual(models.Model):
        nameManual = models.CharField(max_length=70,verbose_name='Наименование')
        typeManual = models.CharField(null=False, blank=False, default='',max_length=70, choices=(('common','Простой'),('time series','Временной ряд')),verbose_name='Тип')

        class Meta:
            verbose_name = 'Создать справочник'
            verbose_name_plural = 'Создать справочники'

        def __str__(self):
            return self.nameManual
