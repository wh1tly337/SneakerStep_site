from datetime import datetime

import pytz
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import OrdersForm, ContactForm, RefoundForm, CatalogForm
from .models import AssortmentAdding, Orders


def home(request):
    items = AssortmentAdding.objects.all()

    return render(request, 'main/home.html', {'items': items})


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

    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items': items,
        'form': form,
        'temp': temp,
        'page_obj': page_obj
    }

    return render(
        request, 'main/shoe_catalog.html', context
    )


def about_us(request):
    return render(template_name='main/about_us.html', request=request)


def chect_out(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase')

    form = OrdersForm()

    return render(request, 'main/out_form.html', {'form': form})


def comming_soon(request):
    return render(template_name='main/comming_soon.html', request=request)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appeal')

    form = ContactForm()

    return render(request, 'main/contact_us.html', {'form': form})


class ProductCard(DetailView):
    model = AssortmentAdding
    template_name = f"main/product_card.html"
    context_object_name = 'item'


def your_cart(request):
    return render(template_name='main/cart.html', request=request)


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

    return render(request, 'main/refound.html', {'form': form})


def purchase(request):
    return render(template_name='main/purchase.html', request=request)


def appeal(request):
    return render(template_name='main/appeal.html', request=request)
