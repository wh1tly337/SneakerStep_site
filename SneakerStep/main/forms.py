from .models import Orders, ContactUs
from django.forms import ModelForm, TextInput, RadioSelect


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = [
            'first_name', 'last_name', 'city',
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
            'last_name': TextInput(attrs={
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


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'contact_name', 'contact_email', 'contact_description',
        ]

        widgets = {
            'contact_name': TextInput(attrs={
                'type': 'text',
                'id': 'contact_name',
                'name': 'contact_name',
                'placeholder': 'Имя',
                'style': 'width: 100%; height: 50px; font-weight: 300;'
            }),
            'contact_email': TextInput(attrs={
                'type': 'text',
                'id': 'contact_email',
                'name': 'contact_email',
                'placeholder': 'Электронная почта',
                'style': 'width: 100%; height: 50px; font-weight: 300;'
            }),
            'contact_description': TextInput(attrs={
                'type': 'text',
                'id': 'contact_description',
                'name': 'contact_description',
                'placeholder': 'Ваше предложение',
                'style': 'width: 100%; height: 150px; font-family: "Poppins", sans-serif; font-weight: 300;'
            }),
        }


class RefoundForm(ModelForm):
    class Meta:
        model = Orders
        fields = [
            'first_name', 'last_name', 'phone_number',
            'email', 'refound_id', 'refound_description'
        ]

        widgets = {
            'first_name': TextInput(attrs={
                'type': 'text',
                'id': 'first_name',
                'name': 'first_name',
                'placeholder': 'Имя',
                # 'style': 'width: 100%; height: 50px; font-weight: 300;'
            }),
            'last_name': TextInput(attrs={
                'type': 'text',
                'id': 'last_name',
                'name': 'last_name',
                'placeholder': 'Фамилия',
                # 'style': 'width: 100%; height: 50px; font-weight: 300;'
            }),
            'phone_number': TextInput(attrs={
                'type': 'text',
                'id': 'phone_number',
                'name': 'phone_number',
                'placeholder': 'Номер телефона',
                # 'style': 'width: 100%; height: 150px; font-family: "Poppins", sans-serif; font-weight: 300;'
            }),
            'email': TextInput(attrs={
                'type': 'text',
                'id': 'email',
                'name': 'email',
                'placeholder': 'Электронная почта',
                # 'style': 'width: 100%; height: 150px; font-family: "Poppins", sans-serif; font-weight: 300;'
            }),
            'refound_id': TextInput(attrs={
                'type': 'text',
                'id': 'refound_id',
                'name': 'refound_id',
                'placeholder': 'Номер заказа',
                # 'style': 'width: 100%; height: 150px; font-family: "Poppins", sans-serif; font-weight: 300;'
            }),
            'refound_description': TextInput(attrs={
                'type': 'text',
                'id': 'refound_description',
                'name': 'refound_description',
                'placeholder': 'Причина возврата',
                # 'style': 'width: 100%; height: 150px; font-family: "Poppins", sans-serif; font-weight: 300;'
            }),
        }
