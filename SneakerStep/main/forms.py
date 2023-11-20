from .models import Orders, ContactUs, Cart, AssortmentAdding
from django import forms
from django.forms import ModelForm, TextInput, RadioSelect


class CatalogForm(forms.Form):
    sort_choices = (
        ('1', 'По популярности'),
        ('2', 'По цене (по убыванию)'),
        ('3', 'По цене (по возрастанию)'),
        ('4', 'По новизне'),
    )

    sort_field = forms.ChoiceField(
        choices=sort_choices,
        label=False,
        widget=forms.Select(attrs={
            'onchange': 'submit()',
            'style': 'border-color: white; outline:none; width: 200px; margin-left: 5px'
        })
    )


class SizeForm(forms.Form):
    size_field = forms.ChoiceField(
        choices=(),
        label=False,
        widget=forms.Select(attrs={
            'style': 'border-color: white; outline:none; width: 140px'
        })
    )

    def __init__(self, currentid, *args, **kwargs):
        super(SizeForm, self).__init__(*args, **kwargs)

        sizes = AssortmentAdding.objects.filter(id=currentid)
        sizes = sizes[0].get_sizes().split(' ')
        self.fields['size_field'].choices = ('0', 'Выберете размер'),
        counter = 0
        for x in range(len(sizes)):
            if sizes[x] == '':
                self.fields['size_field'].choices += (-1, f"{36+counter} - размер отсутствует"),
            else:
                self.fields['size_field'].choices += (sizes[x], sizes[x]),
            counter += 1


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
            }),
            'last_name': TextInput(attrs={
                'type': 'text',
                'id': 'last_name',
                'name': 'last_name',
                'placeholder': 'Фамилия',
            }),
            'phone_number': TextInput(attrs={
                'type': 'text',
                'id': 'phone_number',
                'name': 'phone_number',
                'placeholder': 'Номер телефона'
            }),
            'email': TextInput(attrs={
                'type': 'text',
                'id': 'email',
                'name': 'email',
                'placeholder': 'Электронная почта',
            }),
            'refound_id': TextInput(attrs={
                'type': 'text',
                'id': 'refound_id',
                'name': 'refound_id',
                'placeholder': 'Номер заказа',
            }),
            'refound_description': TextInput(attrs={
                'type': 'text',
                'id': 'refound_description',
                'name': 'refound_description',
                'placeholder': 'Причина возврата',
            }),
        }
