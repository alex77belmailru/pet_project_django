from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
def stages(request):
    data = {'title': 'Главная страница'}
    return render(request, 'orders/stages.html', data)

def cook(request):
    return HttpResponse("<h1>Заказы, которые надо приготовить</h1>")

def deliveryman(request):
    return HttpResponse("<h1>Заказы, которые надо доставить</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")