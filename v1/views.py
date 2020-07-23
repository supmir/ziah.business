from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .models import Content
from .models import Category
# Create your views here.


def products(request, category="Maxxima"):
    maxxima_products = Product.objects.filter(category=str("Maxxima"))
    garden_products = Product.objects.filter(category=str("Garden"))
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'category': category,
        'products': products,
    }
    return render(request, 'v1/products.html', context)


def product(request, category, productname):
    product = get_object_or_404(Product, pk=str(productname))
    content = Content.objects.filter(product=str(productname))
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'category': category,
        'product': product,
        'content': content,
    }
    if category == "Maxxima":
        return render(request, 'v1/product.html', context)
    elif category == "Garden":
        return render(request, 'v1/product.html', context)
    else:
        return HttpResponseNotFound()
