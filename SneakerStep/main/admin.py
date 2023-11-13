from django.contrib import admin
from .models import *


class AdminAssortment(admin.ModelAdmin):
    list_display = ('name', 'id', 'date', 'price')
    search_fields = ('id', 'name', 'price', 'description')
    list_filter = ('date',)
    empty_value_display = '-пусто-'


class AdminOrders(admin.ModelAdmin):
    list_display = ('order_id', 'status', 'first_name')
    search_fields = (
        'order_id', 'items', 'first_name',
        'lastname', 'city', 'post_index',
        'adres', 'phone_number', 'email'
    )
    list_filter = ('start_date', 'status')
    empty_value_display = '-пусто-'


class AdminContact(admin.ModelAdmin):
    list_display = ('contact_id', 'contact_name', 'contact_date', 'contact_email')
    search_fields = ('contact_id', 'contact_name', 'contact_description', 'contact_email')
    list_filter = ('contact_date',)
    empty_value_display = '-пусто-'


admin.site.register(AssortmentAdding, AdminAssortment)
admin.site.register(Orders, AdminOrders)
admin.site.register(ContactUs, AdminContact)
