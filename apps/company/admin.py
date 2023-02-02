from django.contrib import admin
from company.models import (
    Pen,
    Quantity
)
# Register your models here.


class PenAdmin(admin.ModelAdmin):
    model = Pen
    list_display = [
        'title',
        'form',
        'color'
    ]


class QuantityAdmin(admin.ModelAdmin):
    model = Quantity
    list_display = [
        'number',
        'quantity_of_pen',
    ]


admin.site.register(Pen, PenAdmin)
admin.site.register(Quantity, QuantityAdmin)
