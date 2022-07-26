# Generated by Django 4.0.6 on 2022-07-25 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manual', '0009_delete_createprice_remove_createsale_typesale_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Наименование')),
                ('date', models.DateTimeField()),
                ('formula', models.TextField(verbose_name='Формула')),
                ('is_constant', models.BooleanField(default=False, verbose_name='Константа')),
                ('period_start', models.DateField(verbose_name='Начальная дата')),
                ('period_end', models.DateField(verbose_name='Конечная дата')),
                ('calculated_value', models.FloatField(verbose_name='Вычисляемое значение')),
                ('expected_value', models.FloatField(verbose_name='Ожидаемое значение')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Продукт', 'Продукт'), ('Услуга', 'Услуга')], default='', max_length=25, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('Услуга', '-'), ('Кг', 'КГ'), ('Гр', 'Г'), ('Шт', 'ШТ'), ('Л', 'Л'), ('Упаковка', 'УПАК')], default='', max_length=40, verbose_name='Единицы измерения')),
            ],
        ),
        migrations.CreateModel(
            name='CreateSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_type', models.CharField(choices=[('day', 'День'), ('month', 'Месяц'), ('quarter', 'Квартал'), ('year', 'Год')], default='День', max_length=10, verbose_name='Тип временного периода')),
                ('period_start', models.DateField(verbose_name='Начало временного периода')),
                ('period_end', models.DateField(verbose_name='Конец временного периода')),
                ('value_nat', models.FloatField(default='', max_length=10, verbose_name='Значение')),
                ('typeSale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_of_Types_Sale', to='manual.type')),
                ('unitSale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_of_Units_Sale', to='manual.unit')),
            ],
            options={
                'verbose_name': 'Создать объём продаж',
                'verbose_name_plural': 'Создать объемы продаж',
            },
        ),
        migrations.CreateModel(
            name='CreateProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Наименование')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('typeProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_of_Types_Prod', to='manual.type')),
                ('unitProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_of_Units_Prod', to='manual.unit')),
            ],
            options={
                'verbose_name': ('Добавить товар/услугу',),
                'verbose_name_plural': 'Добавить товары/услуги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CreatePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('period_type', models.CharField(choices=[('День', 'День'), ('Месяц', 'Месяц'), ('Квартал', 'Квартал'), ('Год', 'Год')], default='День', max_length=10)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('price_non_nds', models.IntegerField(default=0, verbose_name='Цена без NDS')),
                ('NDS_type', models.IntegerField(choices=[(0, '0'), (10, '10'), (20, '20')], default='0')),
                ('NDS', models.FloatField(default=0, verbose_name='НДС')),
                ('price_with_nds', models.FloatField(default=0, verbose_name='Цена с НДС')),
                ('typePrice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_of_Types_Price', to='manual.type')),
            ],
            options={
                'verbose_name': 'Создать цену',
                'verbose_name_plural': 'Создать цены',
                'ordering': ['-date'],
            },
        ),
    ]
