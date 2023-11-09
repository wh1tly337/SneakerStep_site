from .models import Orders
from django.forms import ModelForm, TextInput, RadioSelect


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = [
            'first_name', 'lastname', 'city',
            'post_index', 'adres', 'phone_number',
            'email', 'payment_method'
        ]
        choices = (
            ('Картой онлайн', 'Картой онлайн'),
            ('Картой при получении', 'Картой при получении'),
            ('Наличными при получении', 'Наличными при получении')
        )

        widgets = {
            'first_name': TextInput(attrs={
                'type': 'text',
                'id': 'firstname',
                'name': 'firstname',
                'placeholder': 'Имя',
                'style': 'width: 47%; height: 40px; margin: 10px 6px 10px 15px'
            }),
            'lastname': TextInput(attrs={
                'type': 'text',
                'id': 'lastname',
                'name': 'lastname',
                'placeholder': 'Фамилия',
                'style': 'width: 47%; height: 40px; margin: 10px 0 10px 6px'
            }),
            'city': TextInput(attrs={
                'type': 'text',
                'id': 'city',
                'name': 'city',
                'placeholder': 'Город/Населенный пункт',
                'style': 'width: 97%; height: 40px; margin: 10px 0 10px 15px'
            }),
            'post_index': TextInput(attrs={
                'type': 'text',
                'id': 'postcode',
                'name': 'postcode',
                'placeholder': 'Почтовый индекс',
                'style': 'width: 97%; height: 40px; margin: 10px 0 10px 15px'
            }),
            'adres': TextInput(attrs={
                'type': 'text',
                'id': 'adres',
                'name': 'adres',
                'placeholder': 'Адрес',
                'style': 'width: 97%; height: 40px; margin: 10px 0 10px 15px'
            }),
            'phone_number': TextInput(attrs={
                'type': 'text',
                'id': 'phone',
                'name': 'phone',
                'placeholder': 'Номер телефона',
                'style': 'width: 47%; height: 40px; margin: 10px 6px 10px 15px'
            }),
            'email': TextInput(attrs={
                'type': 'text',
                'id': 'email',
                'name': 'email',
                'placeholder': 'Электронная почта',
                'style': 'width: 47%; height: 40px; margin: 10px 0 10px 6px'
            }),
            'payment_method': RadioSelect(attrs={
                'name': 'rating',
                'style': 'margin-left: -5px'
            }, choices=choices)
        }
