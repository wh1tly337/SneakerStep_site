from django.db import models
from django.core.validators import RegexValidator


def user_directory_path(instance, filename):
    return 'static/main/images_new/assortment/{0}/{1}'.format(instance.id, filename)


class AssortmentAdding(models.Model):
    id = models.AutoField('ID вещи', primary_key=True)
    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    # [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
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
        return self.name

    class Meta:
        verbose_name = 'Добавление ассортимента'
        verbose_name_plural = 'Добавление ассортимента'


class Orders(models.Model):
    status_choices = (
        ('Decorated', 'Оформлен'),
        ('Sent', 'Отправлен'),
        ('Completed', 'Завершен'),
        ('Cancelled', 'Отменен'),
        ('Refund', 'Возврат'),
    )

    order_id = models.AutoField('ID заказа', primary_key=True)
    status = models.CharField('Статус заказа', choices=status_choices, max_length=10)
    items = models.IntegerField('ID заказанных вещей')
    # TODO придумать как передавать массив заказов, если их больше одного
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)
    city = models.CharField('Город', max_length=50)
    adres = models.CharField('Адрес', max_length=100)
    post_index = models.CharField('Почтовый индекс', max_length=10)
    phone_regex = RegexValidator(
        regex=r"\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}",
        message="Номер телефона должен быть в формате: '+79999999999'."
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        validators=[phone_regex],
        max_length=12
    )
    email = models.EmailField('Электронная почта')
    start_date = models.DateField('Дата оформления заказа')
    end_date = models.DateField('Дата завершения заказа')

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

# class HomePageUpdater(models.Model):
#     id = models.AutoField('ID вещи', primary_key=True)
