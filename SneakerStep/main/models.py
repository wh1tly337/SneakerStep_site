from django.db import models
import django


def user_directory_path(instance, filename):
    return 'static/main/images_new/assortment/{0}/{1}'.format(instance.name, filename)


class AssortmentAdding(models.Model):
    id = models.AutoField('ID вещи', primary_key=True)
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
    date = models.DateField('Дата добавления')

    def __str__(self):
        return f"ID товара: {str(self.id)}"

    class Meta:
        verbose_name = 'Добавление ассортимента'
        verbose_name_plural = 'Добавление ассортимента'


class Orders(models.Model):
    status_choices = (
        ('Оформлен', 'Оформлен'),
        ('Отправлен', 'Отправлен'),
        ('Завершен', 'Завершен'),
        ('Отменен', 'Отменен'),
        ('Возврат', 'Возврат'),
    )

    order_id = models.AutoField('ID заказа', primary_key=True)
    status = models.CharField('Статус заказа', choices=status_choices, max_length=10, default='Оформлен')
    items = models.CharField('ID заказанных вещей', max_length=100)
    first_name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия', max_length=50)
    city = models.CharField('Город', max_length=50)
    post_index = models.CharField('Почтовый индекс', max_length=10)
    adres = models.CharField('Адрес', max_length=100)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12)
    email = models.EmailField('Электронная почта')
    payment_method = models.CharField('Способ оплаты', max_length=30, default='OnlineCard')
    start_date = models.DateField('Дата оформления заказа', default=django.utils.timezone.now)

    def __str__(self):
        return f"ID заказа: {str(self.order_id)}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class ContactUs(models.Model):
    contact_id = models.AutoField('ID обращения', primary_key=True)
    contact_date = models.DateField('Дата обращения', default=django.utils.timezone.now)
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
