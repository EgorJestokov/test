from django.contrib import admin

from manual.models import Indicator, CreateItemMod, Price


class CreateItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'unit', 'price')
    list_filter = ('unit', 'type')
    list_editable = ('name', 'type', 'unit', 'price')
    search_fields = ('id', 'name', 'type', 'unit', 'price')


admin.site.register(Indicator)
admin.site.register(Price)
admin.site.register(CreateItemMod, CreateItemAdmin)
