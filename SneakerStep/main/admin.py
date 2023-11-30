import csv
import os
from datetime import datetime

import pytz
from django.contrib import admin
from django.db.models import QuerySet, Count, Sum
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
        'set_status_cancelled', 'make_pdf',
        'make_pdf_refound'
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

    @admin.action(description='Создать PDF отчет')
    def make_pdf(self, request, qs: QuerySet):
        current_date = datetime.now().strftime("%d/%m/%Y")

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # response['Content-Disposition'] = 'attachment; filename="фывфыв.pdf"'

        document = canvas.Canvas(response, pagesize=A4)

        pdfmetrics.registerFont(TTFont('calibri', os.path.join('static/main/fonts/calibri.ttf')))

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 40, 'Отчет по заказам "СникерШаг"')

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 60, f"Дата формирования: {current_date}")

        col_widths = [1 * cm, 2 * cm, 2 * cm, 1.5 * cm, 3 * cm, 2.5 * cm, 1.1 * cm, 2 * cm, 2 * cm, 2 * cm]

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

        indent = 70

        for status_info in Orders.objects.exclude(status='Возврат').values('status').annotate(total=Count('status')):
            data = [[
                'ID', 'Статус', 'ID вещи\n(разм)', 'Наимен',
                'Сумма', 'Покуп',
                'Город', 'Способ\nоплаты', 'Дата\nоформл',
                'Дата\nобновл'
            ]]
            status = status_info.get('status')
            total = status_info.get('total')

            for order in Orders.objects.filter(status=status):
                username = str(order.last_name) + '\n' + str(order.first_name)

                try:
                    start_date = str(order.start_date)[:-13]
                    start_date = start_date.replace(' ', '\n')
                except Exception:
                    start_date = ''

                try:
                    update_date = str(order.end_date)[:-6]
                    update_date = update_date.replace(' ', '\n')
                except Exception:
                    update_date = ''

                try:
                    payment_method = order.payment_method
                    payment_method = payment_method.replace(' ', '\n')
                except Exception:
                    payment_method = ''

                try:
                    if order.city == 'Екатеринбург':
                        city = 'ЕКБ'
                    else:
                        city = 'noname'
                except Exception:
                    city = 'noname'

                try:
                    name = order.items_names
                    name = name.split(' ')
                    name = '\n'.join(name[:4])
                except Exception:
                    name = ''

                data.append([
                    order.order_id, order.status, order.items_id, name,
                    order.final_price, username,
                    city, payment_method,
                    start_date, update_date
                ])

            final_price = Orders.objects.values('status').filter(status=status).annotate(sum=Sum('final_price'))
            data.append(['', '', '', '', '', '', '', '', '', ''])
            data.append([
                '', '', '',
                'Итого:', final_price[0].get('sum'),
                '', '', '', '', ''
            ])

            table = Table(data, col_widths)

            table.setStyle(style)
            table.wrapOn(document, 350, 0)
            indent = indent + 60 + (total * 50) + 40
            table.drawOn(document, A4[0] / 15, A4[1] - indent)

            page_number = document.getPageNumber()
            document.setFont("calibri", 14)
            document.drawString(A4[0] / 1.33, A4[1] - 60, f"Номер страницы: {page_number}")

        data = [[]]
        final_price_sum = Orders.objects.exclude(status='Возврат').aggregate(sum=Sum('final_price')).get('sum')
        data.append([
            '', '', 'Итого по всем заказам:',
            '', final_price_sum,
            '', '', '', '', ''
        ])
        style = TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'calibri'),
            ('FONTNAME', (0, 1), (-1, -1), 'calibri'),
            ('FONTSIZE', (0, 0), (-1, -1), 16),
            ('FONTSIZE', (0, 1), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 14),
            ('BACKGROUND', (0, 1), (-1, -1), '#ECECEC')
        ])
        table = Table(data, col_widths)
        table.setStyle(style)
        table.wrapOn(document, 350, 0)
        indent = indent + 40
        table.drawOn(document, A4[0] / 15, A4[1] - indent)

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 800, f"Должность: _____________")

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 3, A4[1] - 800, f"      _____________         Расшифровка: _____________")

        # document.showPage()
        document.save()

        return response

    @admin.action(description='Создать PDF отчет по возвратам')
    def make_pdf_refound(self, request, qs: QuerySet):
        current_date = datetime.now().strftime("%d/%m/%Y")

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report_refount.pdf"'
        # response['Content-Disposition'] = 'attachment; filename="фывфыв.pdf"'

        document = canvas.Canvas(response, pagesize=A4)

        pdfmetrics.registerFont(TTFont('calibri', os.path.join('static/main/fonts/calibri.ttf')))

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 40, 'Отчет по возвратам "СникерШаг"')

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 60, f"Дата формирования: {current_date}")

        col_widths = [1 * cm, 2 * cm, 2 * cm, 1.5 * cm, 3 * cm, 2.5 * cm, 1.1 * cm, 2 * cm, 2 * cm, 2 * cm]

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

        indent = 70

        data = [[
            'ID', 'Причина\nвозрата', 'ID вещи\n(разм)',
            'Сумма', 'Покупатель',
            'Город', 'Способ\nоплаты', 'Дата\nоформл',
            'Дата\nобновл'
        ]]
        status_info = Orders.objects.filter(status='Возврат').values('status').annotate(total=Count('status'))
        status = status_info[0].get('status')
        total = status_info[0].get('total')

        for order in Orders.objects.filter(status=status):
            username = str(order.last_name) + '\n' + str(order.first_name)

            try:
                start_date = str(order.start_date)[:-13]
                start_date = start_date.replace(' ', '\n')
            except Exception:
                start_date = ''

            try:
                update_date = str(order.end_date)[:-6]
                update_date = update_date.replace(' ', '\n')
            except Exception:
                update_date = ''

            try:
                payment_method = order.payment_method
                payment_method = payment_method.replace(' ', '\n')
            except Exception:
                payment_method = ''

            try:
                refound_description = order.refound_description
                refound_description = refound_description.replace(' ', '\n')
            except Exception:
                refound_description = ''

            try:
                if order.city == 'Екатеринбург':
                    city = 'ЕКБ'
                else:
                    city = 'noname'
            except Exception:
                city = 'noname'

            try:
                name = order.items_names
                name = name.split(' ')
                name = '\n'.join(name[:4])
            except Exception:
                name = ''

            data.append([
                order.order_id, refound_description, order.items_id,name,
                order.final_price, username,
                city, payment_method,
                start_date, update_date
            ])

        final_price = Orders.objects.values('status').filter(status=status).annotate(sum=Sum('final_price'))
        data.append(['', '', '', '', '', '', '', '', '', ''])
        data.append([
            '', '','',
            'Итого:', final_price[0].get('sum'),
            '', '', '', '', ''
        ])

        table = Table(data, col_widths)

        table.setStyle(style)
        table.wrapOn(document, 350, 0)
        indent = indent + 60 + (total * 50) + 40
        table.drawOn(document, A4[0] / 15, A4[1] - indent)

        page_number = document.getPageNumber()
        document.setFont("calibri", 14)
        document.drawString(A4[0] / 1.33, A4[1] - 60, f"Номер страницы: {page_number}")

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 15, A4[1] - 800, f"Должность: _____________")

        document.setFont("calibri", 14)
        document.drawString(A4[0] / 3, A4[1] - 800, f"      _____________         Расшифровка: _____________")

        # document.showPage()
        document.save()

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
