from rest_framework import serializers
from .models import FabricOrder, FabricOrderItem

class FabricOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricOrderItem
        fields = ['item_qty', 'gsm', 'finish_dia', 'machine_dia', 'fabric_type']
        

class FabricOrderSerializer(serializers.ModelSerializer):
    order_items = FabricOrderItemSerializer(many=True)

    class Meta:
        model = FabricOrder
        fields = ['buyer_name', 'order_type', 'issue_date', 'shipment_date', 'order_qty', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')

        order = FabricOrder.objects.create(**validated_data)

        total_qty = 0

        for item_data in order_items_data:
            total_qty += item_data['item_qty']
            FabricOrderItem.objects.create(order=order, **item_data)

        order.order_qty = total_qty
        order.save()

        return order
