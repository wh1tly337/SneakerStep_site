from django.contrib import admin
from .models import *


class AdminAssortment(admin.ModelAdmin):
    list_display = ('name', 'id', 'price')
    search_fields = ('id', 'name')
    list_filter = ('date',)
    empty_value_display = '-пусто-'


class AdminOrders(admin.ModelAdmin):
    list_display = ('order_id', 'status', 'first_name')
    search_fields = ('items', 'adres', 'phone_number')
    list_filter = ('start_date',)
    empty_value_display = '-пусто-'


class AdminContact(admin.ModelAdmin):
    list_display = ('contact_id', 'contact_name', 'contact_date', 'contact_email')
    search_fields = ('contact_description',)
    list_filter = ('contact_date',)
    empty_value_display = '-пусто-'


admin.site.register(AssortmentAdding, AdminAssortment)
admin.site.register(Orders, AdminOrders)
admin.site.register(ContactUs, AdminContact)
