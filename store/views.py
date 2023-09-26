from django.shortcuts import render, redirect
from product.models import Product, Category
from django.db.models import Q
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'store/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('base')
    else:
        form = SignUpForm()

    return render(request, 'store/signup.html', {'form': form})


@login_required
def my_account(request):
    return render(request, 'store/myaccount.html')

@login_required
def edit_my_account(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('myaccount')
    return render(request, 'store/edit_myaccount.html')


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {'categories': categories,
               'products': products,
               'active_category': active_category,
               }

    return render(request, 'store/shop.html', context)