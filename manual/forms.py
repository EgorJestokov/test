from django import forms
from .models import CreateProduct, CreatePrice, CreateSale
from django.forms import ModelForm



class formProduct(ModelForm):
    class Meta:
        model = CreateProduct
        fields = '__all__'


class formPrice(ModelForm):
    class Meta:
        model = CreatePrice
        fields = '__all__'


class formSales(ModelForm):
    class Meta:
        model = CreateSale
        fields = '__all__'

# class formCreate(ModelForm):
#     class Meta:
#         model = CreateManual
#         fields = '__all__'

class ModelTest(ModelForm):
    pass