# Generated by Django 4.0.6 on 2022-07-25 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0006_alter_createprice_options_createitemmod_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreatePrice',
        ),
        migrations.DeleteModel(
            name='Indicator',
        ),
        migrations.RemoveField(
            model_name='sales_volume',
            name='typeSale',
        ),
        migrations.RemoveField(
            model_name='sales_volume',
            name='unitSale',
        ),
        migrations.DeleteModel(
            name='CreateItemMod',
        ),
        migrations.DeleteModel(
            name='Sales_Volume',
        ),
    ]
