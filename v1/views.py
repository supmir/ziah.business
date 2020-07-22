from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .models import Content
# Create your views here.


def products(request):
    maxxima_products = Product.objects.filter(product_category=str("maxxima"))
    garden_products = Product.objects.filter(product_category=str("garden"))
    context = {
        'maxxima_products': maxxima_products,
        'garden_products': garden_products
    }
    return render(request, 'v1/products.html', context)


def product(request, category, productname):
    product = get_object_or_404(Product, pk=str(productname))
    # category = getattr(product, "product_category")
    # content = Content.objects.filter(productname=str(productname))
    context = {
    #     'product': product,
    #     'content': content,
    }
    if category == "maxxima":
        return render(request, 'v1/product.html', context)
    elif category == "garden":
        return render(request, 'v1/product.html', context)
    else:
        return HttpResponseNotFound()
