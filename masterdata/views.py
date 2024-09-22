from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from masterdata.serializers import BuyerSerializer,MachineTypeSerializer
from masterdata.models import Buyer,MachineType
from rest_framework.views import APIView


# Using function Base APIVIEW

@api_view(['GET','POST'])
def buyer_list_create(request):
    if request.method == "GET":
        buyers = Buyer.objects.all()
        serializer = BuyerSerializer(buyers,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "messages":"Buyer Create Successfully",
                'data':serializer.data
            },status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                'messages':"Failed To Create Buyer",
                'errors': serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def buyer_show_edit_delete(request,id):
    try:
        buyer = Buyer.objects.get(id=id)
    except Buyer.DoesNotExist:
        return Response({"messages": "Buyer not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BuyerSerializer(buyer)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = BuyerSerializer(buyer,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'messages':'Buyer Updated Successfully',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'messages': 'Failed to buyer update',
                'errors':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        buyer.delete()
        return Response({"messages": "Buyer deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# Using Class Base APIVIEW
class MachineTypeListCreateView(APIView):

    def  get(self,request):
        machine_types = MachineType.objects.all()
        serializer = MachineTypeSerializer(machine_types,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        try:
            serializer = MachineTypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'messages':'Machine Type Created Successfully',
                    'data':serializer.data
                })
            else:
                return Response({
                    "message": "Failed to create Machine Type.",
                    'errors':serializer.errors
                })
        except Exception as e:
            return Response({"message": "An error occurred while creating the machine type.", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MachineTypeShowEditDeleteView(APIView):

    def get(self,request,id):
        try:
            machine_type = MachineType.objects.get(id=id)
            serializer = MachineTypeSerializer(machine_type);
            return Response(serializer.data)
        
        except MachineType.DoesNotExist:
            return Response({"error": "Machine Type not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        try:
            machine_type = MachineType.objects.get(id=id)
            serializer = MachineTypeSerializer(machine_type,data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response({
                    'messages':'Machine Type Updated Successfully',
                    'data':serializer.data
                })
            else:
                return Response({
                'messages': 'Failed to Machine Type update',
                'errors':serializer.errors
                },status=status.HTTP_400_BAD_REQUEST)
        except MachineType.DoesNotExist:
            return Response({"error": "Machine Type not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,id):
        try:
            machine_type = MachineType.objects.get(id=id)
        except MachineType.DoesNotExist:
            return Response({"error": "Machine Type not found."}, status=status.HTTP_404_NOT_FOUND)
        
        machine_type.delete()

        return Response({"msg": "Machine Type deleted successfully"}, status=status.HTTP_204_NO_CONTENT)