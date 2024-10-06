from django.contrib import admin
from .models import MallOrderClass


class MallOrderAdmin(admin.ModelAdmin):
    list_display = ('ordering_user', 'ordering_product')


admin.site.register(MallOrderClass, MallOrderAdmin)
