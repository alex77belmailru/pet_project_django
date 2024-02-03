from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def main_page(request):
    return HttpResponse("<h1>Наш супер-пупер модный сайт для ресторана!!!<h1>")

def index(request):
    return HttpResponse("Сотрудники.")

def cook(request):
    return HttpResponse("<h1>Заказы, которые надо приготовить</h1>")

def deliveryman(request):
    return HttpResponse("<h1>Заказы, которые надо доставить</h1>")