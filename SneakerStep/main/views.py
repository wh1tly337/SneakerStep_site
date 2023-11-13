from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import OrdersForm, ContactForm
from .models import AssortmentAdding


def home(request):
    items = AssortmentAdding.objects.all()

    return render(request, 'main/home.html', {'items': items})


def catalog(request):
    items = AssortmentAdding.objects.all()
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'main/shoe_catalog.html',
        {'items': items, 'page_obj': page_obj}
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
    return render(template_name='main/refound.html', request=request)


def purchase(request):
    return render(template_name='main/purchase.html', request=request)


def appeal(request):
    return render(template_name='main/appeal.html', request=request)
