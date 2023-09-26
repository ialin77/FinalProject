from django.urls import path
from .views import frontpage, shop, signup, my_account, edit_my_account
from product.views import product
from django.contrib.auth import views


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('myaccount/', my_account, name='myaccount'),
    path('myaccount/edit/', edit_my_account, name='edit_my_account'),
    path('login/', views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),

]
