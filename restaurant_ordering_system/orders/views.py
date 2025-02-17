from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from orders.models import Order


def index(request):
    return render(request, 'orders/index.html')


def deliveryman(request):
    return render(request, 'orders/delivery.html')


def orders_man(request):
    order = Order.objects.create(
        name='Егор',
        order='Рис с редиской',
        ready_to_delivery='Нет'
    )
    return HttpResponse('Информация добавлена')


def cook(request):
    orders_to_cook = Order.objects.all()  # Получаем все объекты модели Order из базы данных
    return render(request, 'orders/cook.html', {'orders_to_cook': orders_to_cook})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")