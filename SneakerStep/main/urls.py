from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('about_us', views.about_us, name='about_us'),
    path('chect_out', views.chect_out, name='chect_out'),
    path('comming_soon', views.comming_soon, name='comming_soon'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('product_card/id=<int:pk>', views.ProductCard.as_view(), name='product_card'),
    path('your_cart', views.your_cart, name='your_cart'),
    path('refound', views.refound, name='refound'),
    path('purchase', views.purchase, name='purchase')
]
