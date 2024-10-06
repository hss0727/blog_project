from django.contrib import admin
from .models import MallUserClass


class MallUserAdmin(admin.ModelAdmin):
    list_display = ('user_email',)


admin.site.register(MallUserClass, MallUserAdmin)
