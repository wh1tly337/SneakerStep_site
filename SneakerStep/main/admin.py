import csv
from datetime import datetime

import pytz
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpResponse

from .models import *


class AdminAssortment(admin.ModelAdmin):
    ordering = ('-id',)

    exclude = ('id',)
    actions = ('make_csv',)

    list_display = ('name', 'id', 'price', 'add_date', 'update_date')
    search_fields = ('id', 'name', 'price', 'description')
    list_filter = ('add_date', 'update_date')

    empty_value_display = '-пусто-'

    @admin.action(description='Создать CSV отчет')
    def make_csv(self, request, qs: QuerySet):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="assortment.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'ID товара', 'Название', 'Цена',
            'Размеры', 'Описание', 'Главное изображение',
            'Втророе изображение', 'Третье изображение', 'Дата добавления'
        ])

        items = AssortmentAdding.objects.all().values_list(
            'id', 'name', 'price',
            'sizes', 'description', 'main_image',
            'second_image', 'third_image', 'add_date'
        )
        for item in items:
            writer.writerow(item)

        return response


class AdminOrders(admin.ModelAdmin):
    ordering = ('-order_id',)
    list_per_page = 10

    exclude = ('order_id', 'refound_id')
    actions = (
        'set_status_sent', 'set_status_completed',
        'set_status_cancelled', 'make_csv',
        'make_csv_refound'
    )

    list_display = (
        'order_id', 'status', 'first_name',
        'last_name', 'email', 'start_date',
        'end_date'
    )
    search_fields = (
        'order_id', 'items', 'first_name',
        'last_name', 'city', 'post_index',
        'adres', 'phone_number', 'email'
    )
    list_filter = ('start_date', 'status')

    empty_value_display = '-пусто-'

    @admin.action(description='Установить статус "Отправлен"')
    def set_status_sent(self, request, qs: QuerySet):
        count_updateted = qs.update(
            status=Orders.SENT,
            end_date=datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime("%Y-%m-%d %H:%M:%S")
        )
        self.message_user(
            request,
            f"Статус 'Отправлен' был применен к {count_updateted} записи(ям)"
        )

    @admin.action(description='Установить статус "Завершен"')
    def set_status_completed(self, request, qs: QuerySet):
        count_updateted = qs.update(
            status=Orders.COMPLETED,
            end_date=datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime("%Y-%m-%d %H:%M:%S")
        )
        self.message_user(
            request,
            f"Статус 'Завершен' был применен к {count_updateted} записи(ям)"
        )

    @admin.action(description='Установить статус "Отменен"')
    def set_status_cancelled(self, request, qs: QuerySet):
        count_updateted = qs.update(
            status=Orders.CANCELLED,
            end_date=datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime("%Y-%m-%d %H:%M:%S")
        )
        self.message_user(
            request,
            f"Статус 'Отменен' был применен к {count_updateted} записи(ям)"
        )

    @admin.action(description='Создать CSV отчет')
    def make_csv(self, request, qs: QuerySet):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'ID заказа', 'Статус заказа', 'ID заказанных вещей', 'Наименование заказанной вещи',
            'Сумма заказа', 'Имя', 'Фамилия',
            'Город', 'Способ оплаты', 'Дата оформления заказа',
            'Дата обновления заказа'
        ])

        orders = Orders.objects.all().values_list(
            'order_id', 'status', 'items_id', 'items_names',
            'final_price', 'first_name', 'last_name',
            'city', 'payment_method', 'start_date',
            'end_date'
        )
        for order in orders:
            writer.writerow(order)

        return response

    @admin.action(description='Создать CSV отчет по возвратам')
    def make_csv_refound(self, request, qs: QuerySet):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'ID заказа', 'Статус заказа', 'Причина возврата',
            'ID заказанных вещей', 'Наименование заказанной вещи', 'Сумма заказа',
            'Имя', 'Фамилия', 'Город',
            'Способ оплаты', 'Дата оформления заказа', 'Дата обновления заказа'
        ])

        orders = Orders.objects.filter(status='Возврат').values_list(
            'order_id', 'status', 'refound_description',
            'items_id', 'items_names', 'final_price',
            'first_name', 'last_name', 'city',
            'payment_method', 'start_date', 'end_date'
        )
        for order in orders:
            writer.writerow(order)

        return response


class AdminContact(admin.ModelAdmin):
    ordering = ('-contact_id',)
    list_per_page = 10

    exclude = ('contact_id',)

    list_display = ('contact_id', 'contact_name', 'contact_email', 'contact_date')
    search_fields = ('contact_id', 'contact_name', 'contact_description', 'contact_email')
    list_filter = ('contact_date',)

    empty_value_display = '-пусто-'


admin.site.register(AssortmentAdding, AdminAssortment)
admin.site.register(Orders, AdminOrders)
admin.site.register(ContactUs, AdminContact)
