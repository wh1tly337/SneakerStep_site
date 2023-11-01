from django.shortcuts import render


def home(request):
    return render(template_name='main/Home.html', request=request)


def catalog(request):
    return render(template_name='main/Catalog.html', request=request)


def about_us(request):
    return render(template_name='main/About_us.html', request=request)


def chect_out(request):
    return render(template_name='main/Chect_out.html', request=request)


def comming_soon_page(request):
    return render(template_name='main/Comming_soon_page.html', request=request)


def contact_us(request):
    return render(template_name='main/Contact_us.html', request=request)


def product_card(request):
    return render(template_name='main/Product_card.html', request=request)


def your_cart(request):
    return render(template_name='main/Your_cart.html', request=request)
