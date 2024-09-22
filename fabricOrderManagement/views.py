from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FabricOrder
from fabricOrderManagement.seralizers import FabricOrderSerializer
from rest_framework.generics import ListAPIView

class FabricOrderListView(ListAPIView):
    queryset = FabricOrder.objects.all()
    serializer_class = FabricOrderSerializer


class FabricOrderCreateView(APIView):
    def post(self, request):
        serializer = FabricOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
