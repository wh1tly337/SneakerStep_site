from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('about_us', views.about_us, name='about_us'),
    path('chect_out', views.chect_out, name='chect_out'),
    path('comming_soon_page', views.comming_soon_page, name='comming_soon_page'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('product_card', views.product_card, name='product_card'),
    path('your_cart', views.your_cart, name='your_cart')
]
