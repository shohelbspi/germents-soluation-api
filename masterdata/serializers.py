from rest_framework import serializers
from masterdata.models import Buyer,MachineType,Unit,YarnCount,YarnType

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"
        
class MachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineType
        fields = "__all__"

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

class YarnCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = YarnCount
        fields = '__all__'

class YarnTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YarnType
        fields = '__all__'
