from django.contrib import admin

from manual.models import Indicator, CreateProduct, CreateSale, CreatePrice, CreateManual


class CreateProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity')


class CreateSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'period_type', 'period_start', 'period_end')


class CreatePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'period_type')


admin.site.register(Indicator)
admin.site.register(CreatePrice, CreatePriceAdmin)
admin.site.register(CreateProduct, CreateProductAdmin)
admin.site.register(CreateSale)
admin.site.register(CreateManual)
