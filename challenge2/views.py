# from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from .models import CarList,UsersModel,ShowroomModel
from .api_file.serializers import CarSerializer, UserSerializer,ShowroomSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# import json
# Create your views here.


# def carListView(request):
#     cars=CarList.objects.all()
#     response={
#         "cars":list(cars.values())
#     }
#     data_json=json.dumps(response)
#     return HttpResponse(data_json,content_type="application/json")
#     # return JsonResponse(response)

# def carDetailView(request,pk):
#     car = CarList.objects.get(pk=pk)
#     response = {
#         "name":car.name,
#         "description":car.description,
#         "active":car.active
        
#     }
#     return JsonResponse(response)

@api_view(["GET","POST"])
def carListView(request):
    if request.method == "GET":
        try:
            car = CarList.objects.all()
        except:
            return Response({"error":"car not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            

@api_view(["GET","PUT","DELETE"])
def carDetailView(request,pk):
    if(request.method=="GET"):
        car = CarList.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    if(request.method=="PUT"):
        car = CarList.objects.get(pk=pk)
        serializer = CarSerializer(car,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if(request.method=="DELETE"):
        car = CarList.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
@api_view(["GET","POST"])
def UserListView(request):
    if request.method == "GET":
        try:
            users = UsersModel.objects.all()
        except:
            return Response({"error":"user not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)     
   
        
    
    

class ShowroomView(APIView):
    def get(self,request):
        try:
            showrooms = ShowroomModel.objects.all()
            serializer = ShowroomSerializer(showrooms,many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            serializer = ShowroomSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as errors:
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)
            
            
class ShowroomDetails(APIView):
    def get(self,request,pk):
        try:
            showroom = ShowroomModel.objects.get(pk=pk)
            serializer = ShowroomSerializer(showroom)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as errors:
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        try:
            showroom = ShowroomModel.objects.get(pk=pk)
            serializer = ShowroomSerializer(showroom,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as errors:
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            showroom = ShowroomModel.objects.get(pk=pk)
            showroom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as errors:
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
        

