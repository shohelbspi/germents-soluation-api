
from django.db import models
from django.contrib.auth.models import User

class FabricOrder(models.Model):
    buyer_name = models.CharField(max_length=120)
    order_type = models.CharField(max_length=120)
    order_qty = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    issue_date = models.DateField()
    shipment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.buyer_name
    

class FabricOrderItem(models.Model):
    order = models.ForeignKey(FabricOrder, on_delete=models.CASCADE, related_name='order_items')
    item_qty = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    gsm = models.CharField(max_length=50)
    finish_dia = models.CharField(max_length=50)
    machine_dia = models.CharField(max_length=50)
    fabric_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Item {self.id} for Order {self.order.id}"
