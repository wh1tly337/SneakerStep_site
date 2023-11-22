import csv
import os
from datetime import datetime

import pytz
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

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
        current_date = datetime.now().strftime("%d/%m/%Y")

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # response['Content-Disposition'] = 'attachment; filename="фыв.pdf"'

        # document = canvas.Canvas(response, pagesize=landscape(A4))
        document = canvas.Canvas(response, pagesize=A4)

        pdfmetrics.registerFont(TTFont('calibri', os.path.join('static/main/fonts/calibri.ttf')))

        document.setFont("calibri", 16)
        document.drawString(A4[0] / 15, A4[1] - 50, 'Отчет по заказам "СникерШаг"')

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 80, f"Дата формирования: {current_date}")

        page_number = document.getPageNumber()
        document.setFont("calibri", 14)
        document.drawString(A4[0] / 1.33, A4[1] - 80, f"Номер страницы: {page_number}")

        orders = Orders.objects.all()

        data = [[
            'ID', 'Статус', 'ID вещ\n(разм)',
            'Сумма', 'Покупатель',
            'Город', 'Способ\nоплаты', 'Дата\nоформл',
            'Дата\nобновл'
        ]]
        # 'Наименование вещи' order.items_names

        for order in orders:
            username = str(order.last_name) + '\n' + str(order.first_name)

            try:
                start_date = (str(order.start_date)[:-13]).split(' ')
                start_date.append('\n')
                memory = start_date[1]
                start_date[1] = start_date[2]
                start_date[2] = memory
                start_date = ''.join(start_date)
            except Exception:
                start_date = ' '
            try:
                update_date = (str(order.end_date)[:-6]).split(' ')
                update_date.append('\n')
                memory = update_date[1]
                update_date[1] = update_date[2]
                update_date[2] = memory
                update_date = ''.join(update_date)
            except Exception:
                update_date = ' '

            payment_method = str(order.payment_method).split(' ')
            payment_method.append('\n')
            if len(payment_method) == 3:
                memory = payment_method[1]
                payment_method[1] = payment_method[2]
                payment_method[2] = memory
                payment_method = ''.join(payment_method)
            else:
                payment_method.append('\n')
                memory1 = payment_method[1]
                memory2 = payment_method[2]
                print(memory1, memory2)
                payment_method[1] = payment_method[-1]
                payment_method[2] = memory1
                payment_method[3] = payment_method[-2]
                payment_method[4] = memory2
                payment_method = ''.join(payment_method)

            data.append([
                order.order_id, order.status, order.items_id,
                order.final_price, username,
                order.city, payment_method,
                start_date, update_date
            ])

        table = Table(data)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#D3D3D3'),
            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'calibri'),
            ('FONTNAME', (0, 1), (-1, -1), 'calibri'),
            ('FONTSIZE', (0, 0), (-1, -1), 16),
            ('FONTSIZE', (0, 1), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 14),
            ('BACKGROUND', (0, 1), (-1, -1), '#ECECEC')
        ])

        table.setStyle(style)
        table.wrapOn(document, 350, 0)
        table.drawOn(document, A4[0] / 15, A4[1] - 450)

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 800, f"Дата: _____________")

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 3, A4[1] - 800, f"Подпись: _____________")

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 1.6, A4[1] - 800, f"Расшифровка: _____________")

        document.showPage()
        document.save()

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
