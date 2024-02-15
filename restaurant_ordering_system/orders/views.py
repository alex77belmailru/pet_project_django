from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from orders.models import Order


# Create your views here.

def index(request):
    return render(request, 'orders/index.html')

def cook(request):
    return render(request, 'orders/cook.html')

def deliveryman(request):
    return render(request, 'orders/delivery.html')

def orders_man(request):
    order = Order.objects.create(
        name='Егор',
        order='Рис с редиской',
        delivery=False,
        ready=True
    )
    return HttpResponse('Информация добавлена')
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")