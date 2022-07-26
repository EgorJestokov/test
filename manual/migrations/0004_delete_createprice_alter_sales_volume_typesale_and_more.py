# Generated by Django 4.0.6 on 2022-07-22 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreatePrice',
        ),
        migrations.AlterField(
            model_name='sales_volume',
            name='typeSale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_of_Types_b', to='manual.createitemmod'),
        ),
        migrations.AlterField(
            model_name='sales_volume',
            name='unitSale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_of_Units_b', to='manual.createitemmod'),
        ),
    ]