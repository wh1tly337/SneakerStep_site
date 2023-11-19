from datetime import datetime

import pytz
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import (
    OrdersForm, ContactForm,
    RefoundForm, CatalogForm,
    SizeForm
)
from .models import AssortmentAdding, Orders, Cart


def for_cart():
    cart = Cart.objects.all()
    amount = Cart.objects.aggregate(Sum('price'))['price__sum']
    return cart, amount


def home(request):
    items = AssortmentAdding.objects.all()
    cart, amount = for_cart()

    context = {
        'items': items,
        'amount': amount,
        'cart': cart
    }

    return render(request, 'main/home.html', context)


def catalog(request):
    try:
        temp = request.GET['sort_field']
        form = CatalogForm(initial={'sort_field': temp})
        choices = {
            '1': AssortmentAdding.objects.all(),
            '2': AssortmentAdding.objects.order_by('-price'),
            '3': AssortmentAdding.objects.order_by('price'),
            '4': AssortmentAdding.objects.order_by('-date'),
        }
        items = choices.get(temp)

    except Exception:
        temp = ''
        form = CatalogForm()
        items = AssortmentAdding.objects.all()

    cart, amount = for_cart()

    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items': items,
        'form': form,
        'temp': temp,
        'page_obj': page_obj,
        'amount': amount,
        'cart': cart
    }

    return render(
        request, 'main/shoe_catalog.html', context
    )


def about_us(request):
    cart, amount = for_cart()

    context = {
        'amount': amount,
        'cart': cart
    }
    return render(request, 'main/about_us.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appeal')

    form = ContactForm()
    cart, amount = for_cart()

    context = {
        'form': form,
        'amount': amount,
        'cart': cart
    }

    return render(request, 'main/contact_us.html', context)


def product_card(request, pk):
    item = get_object_or_404(AssortmentAdding, pk=pk)
    form = SizeForm()
    cart, amount = for_cart()
    error, success = '', ''

    if request.method == 'GET':
        try:
            size = request.GET['size_field']

            if size == '0':
                context = {
                    'item': item,
                    'form': form,
                    'error': 'Вы забыли выбрать размер'
                }

                return render(request, 'main/product_card.html', context)
            else:
                info = AssortmentAdding.objects.in_bulk()

                image = info[pk].main_image
                item_id = info[pk].id
                name = str(info[pk].name)
                price = info[pk].price
                success = 'Товар добавлен в корзину'

                Cart.objects.create(
                    item_id=item_id, image=image,
                    name=name, size=size,
                    price=price, quantity=1
                )
        except Exception:
            pass

    context = {
        'item': item,
        'form': form,
        'cart': cart,
        'amount': amount,
        'error': error,
        'success': success
    }

    return render(request, 'main/product_card.html', context)


def cart(request):
    cart, amount = for_cart()
    context = {
        'amount': amount,
        'cart': cart
    }

    if request.method == 'POST':
        item_id, size = request.POST['deletebtn'].split(' ')
        Cart.objects.filter(
            item_id=item_id,
            size=size
        ).delete()

    return render(request, 'main/cart.html', context)


def chect_out(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()

            cart_items = Cart.objects.all()
            result, final_price = '', 0
            for i in range(len(cart_items)):
                item_id = cart_items[i].get_id()
                size = cart_items[i].get_size()
                result += f"{item_id}({size}) "
                final_price += int(cart_items[i].get_price())

                # Удаление размеров из карточки товара
                assortment = AssortmentAdding.objects.filter(id=item_id)
                sizes = assortment[0].get_sizes().split(' ')
                for j in range(len(sizes)):
                    if sizes[j] == size:
                        sizes[j] = ''
                AssortmentAdding.objects.filter(id=item_id).update(
                    sizes=' '.join(sizes)
                )

            # Добавление общей суммы, id товаров и их рахмеров в таблицу с заказами
            Orders.objects.filter(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                city=form.cleaned_data['city'],
                post_index=form.cleaned_data['post_index'],
                adres=form.cleaned_data['adres'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                payment_method=form.cleaned_data['payment_method'],
            ).update(
                items=result,
                final_price=final_price
            )

            # Удаление всех данных из корзины
            Cart.objects.all().delete()

            return redirect('purchase')

    form = OrdersForm()
    cart, amount = for_cart()

    context = {
        'form': form,
        'amount': amount,
        'cart': cart
    }

    return render(request, 'main/out_form.html', context)


def refound(request):
    if request.method == 'POST':
        form = RefoundForm(request.POST)
        if form.is_valid():
            info = Orders.objects.in_bulk()
            first_name = info[form.cleaned_data['refound_id']].first_name
            last_name = info[form.cleaned_data['refound_id']].last_name
            phone = info[form.cleaned_data['refound_id']].phone_number
            email = info[form.cleaned_data['refound_id']].email
            if (
                    phone == form.cleaned_data['phone_number']
                    and email == form.cleaned_data['email']
                    and first_name == form.cleaned_data['first_name']
                    and last_name == form.cleaned_data['last_name']
            ):
                Orders.objects.filter(order_id=form.cleaned_data['refound_id']).update(
                    status=Orders.REFOUND,
                    refound_description=form.cleaned_data['refound_description'],
                    end_date=datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime("%Y-%m-%d %H:%M:%S")
                )

                return redirect('appeal')
            else:
                return render(request, 'main/refound.html', {
                    'form': form,
                    'error': 'Такого заказа нет, проверьте правильность введенных данных'
                })

        print(form.errors)

    form = RefoundForm()
    cart, amount = for_cart()

    context = {
        'form': form,
        'amount': amount,
        'cart': cart
    }

    return render(request, 'main/refound.html', context)


def purchase(request):
    cart, amount = for_cart()

    context = {
        'amount': amount,
        'cart': cart
    }

    return render(request, 'main/purchase.html', context)


def appeal(request):
    cart, amount = for_cart()

    context = {
        'amount': amount,
        'cart': cart
    }

    return render(request, 'main/appeal.html', context)


def comming_soon(request):
    cart, amount = for_cart()

    context = {
        'amount': amount,
        'cart': cart
    }

    return render(request, 'main/comming_soon.html', context)
