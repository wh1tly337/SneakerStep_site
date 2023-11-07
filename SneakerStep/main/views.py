from django.shortcuts import render
from .models import AssortmentAdding
from django.views.generic import DetailView


def home(request):
    items = AssortmentAdding.objects.all()

    return render(request, 'main/home.html', {'items': items})


def catalog(request):
    items = AssortmentAdding.objects.all()

    return render(request, 'main/shoe_catalog.html', {'items': items})


def about_us(request):
    return render(template_name='main/about_us.html', request=request)


def chect_out(request):
    return render(template_name='main/out_form.html', request=request)


def comming_soon(request):
    return render(template_name='main/comming_soon.html', request=request)


def contact_us(request):
    return render(template_name='main/contact_us.html', request=request)


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
