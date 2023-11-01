from django.shortcuts import render


def home(request):
    return render(template_name='main/home.html', request=request)


def catalog(request):
    return render(template_name='main/shoe_catalog.html', request=request)


def about_us(request):
    return render(template_name='main/about_us.html', request=request)


def chect_out(request):
    return render(template_name='main/out_form.html', request=request)


def comming_soon(request):
    return render(template_name='main/comming_soon.html', request=request)


def contact_us(request):
    return render(template_name='main/contact_us.html', request=request)


def product_card(request):
    return render(template_name='main/product_card.html', request=request)


def your_cart(request):
    return render(template_name='main/cart.html', request=request)


def refound(request):
    return render(template_name='main/refound.html', request=request)


def purchase(request):
    return render(template_name='main/purchase.html', request=request)
