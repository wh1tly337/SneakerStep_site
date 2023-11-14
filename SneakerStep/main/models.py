from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    return 'static/main/images_new/assortment/{0}/{1}'.format(instance.name, filename)


class AssortmentAdding(models.Model):
    id = models.IntegerField('ID товара', primary_key=True)
    name = models.CharField('Название', max_length=100)
    price = models.IntegerField('Цена')
    sizes = models.CharField('Размеры', max_length=50, default='36 37 38 39 40 41 42 43 44 45')
    description = models.TextField('Описание')
    main_image = models.ImageField(
        verbose_name='Главное изображение',
        upload_to=user_directory_path)
    second_image = models.ImageField(
        verbose_name='Втророе изображение',
        upload_to=user_directory_path)
    third_image = models.ImageField(
        verbose_name='Третье изображение',
        upload_to=user_directory_path)
    date = models.DateTimeField('Дата добавления')

    def __str__(self):
        return f"ID товара: {str(self.id)}"

    class Meta:
        verbose_name = 'Добавление ассортимента'
        verbose_name_plural = 'Добавление ассортимента'


class Orders(models.Model):
    DECORATED = 'Оформлен'
    SENT = 'Отправлен'
    COMPLETED = 'Завершен'
    CANCELLED = 'Отменен'
    REFOUND = 'Возврат'
    STATUS_CHOICES = (
        (DECORATED, 'Оформлен'),
        (SENT, 'Отправлен'),
        (COMPLETED, 'Завершен'),
        (CANCELLED, 'Отменен'),
        (REFOUND, 'Возврат'),
    )

    order_id = models.IntegerField('ID заказа', primary_key=True)
    status = models.CharField('Статус заказа', choices=STATUS_CHOICES, max_length=10, default='Оформлен')
    refound_id = models.IntegerField('ID для оформления возврата', blank=True, null=True)
    refound_description = models.TextField('Причина возврата', blank=True, null=True)
    items = models.CharField('ID заказанных вещей', max_length=100)
    final_price = models.IntegerField('Сумма заказа', blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    city = models.CharField('Город', max_length=50)
    post_index = models.CharField('Почтовый индекс', max_length=10)
    adres = models.CharField('Адрес', max_length=100)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12)
    email = models.EmailField('Электронная почта')
    payment_method = models.CharField('Способ оплаты', max_length=30, blank=True, null=True)
    start_date = models.DateTimeField('Дата оформления заказа', default=timezone.now)
    end_date = models.DateTimeField('Дата обновления заказа', blank=True, null=True)

    def __str__(self):
        return f"ID заказа: {str(self.order_id)}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class ContactUs(models.Model):
    contact_id = models.IntegerField('ID обращения', primary_key=True)
    contact_date = models.DateTimeField('Дата обращения', default=timezone.now)
    contact_name = models.CharField('Имя', max_length=100)
    contact_email = models.EmailField('Электронная почта')
    contact_description = models.TextField('Обращение')

    def __str__(self):
        return f"ID обращения: {str(self.contact_id)}"

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

# class HomePageUpdater(models.Model):
#     id = models.AutoField('ID вещи', primary_key=True)
