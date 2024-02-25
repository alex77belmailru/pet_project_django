from django.urls import path
from django.contrib.auth import views as auth_views
from users.apps import UsersConfig
from users import views as custom_views

app_name = UsersConfig.name

urlpatterns = [

]
