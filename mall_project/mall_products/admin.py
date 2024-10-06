from django.contrib import admin
from .models import MallProductClass


class MallProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price')


admin.site.register(MallProductClass, MallProductAdmin)
