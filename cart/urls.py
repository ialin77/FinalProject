from django.urls import path
from cart.views import cart, checkout, add_to_cart, hx_menu_cart, update_cart, hx_cart_total, success, remove_from_cart, change_quantity

urlpatterns = [
    path('', cart, name='cart'),
    path('success/', success, name='success'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('remove-from-cart/<str:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('change-quantity/<str:product_id>/', change_quantity, name='change_quantity'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total')
]