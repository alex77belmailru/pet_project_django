from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page), #http://127.0.0.1:8000/
    path('stages/', views.stages),  #http://127.0.0.1:8000/stages/
    path('cook/', views.cook),    #http://127.0.0.1:8000/cook/
    path('delivery/', views.deliveryman),   #http://127.0.0.1:8000/delivery/
    path('add_info/', views.orders_man),   #http://127.0.0.1:8000/add_info/
]