from django.db import models

class Order(models.Model):
    """Заказ, который сделал клиент"""
    menu_dish = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.menu_dish

# Create your models here.
