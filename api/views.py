from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

class StudentApiView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city','name']
    
    # def get(self,request,format=None):
        
    #     stu = Student.objects.all()
    #     serializer = StudentSerializer(stu,many=True)
    #     return Response(serializer.data)
    
    # def post(self,request,format=None):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Data Created'},serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
# class StudentApiUpdate(APIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['city']

#     def get(self,request,pk=None,format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         return Response({'msg':'Invalid Id'},status=status.HTTP_400_BAD_REQUEST)
    
    
#     def put(self,request,pk=None,format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu,data=request.data,partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Data Updated'})
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk=None,format=None):
#         id=pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             stu.delete()
#             return Response({'msg':'Data Deleted!!!'})            