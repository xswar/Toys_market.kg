from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Product, Order, OrderItem


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


def order_create(request):
    if request.method == 'POST':
        # Обработка данных формы заказа, сохранение заказа и создание связанных позиций заказа
        # ...
        return render(request, 'store/order_created.html')
    else:
        return render(request, 'store/order_create.html')

