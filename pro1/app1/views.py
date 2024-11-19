from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import ContactSerializer,EducationdetailSerializer,FamilydetailsSerializer,PartnerprefarencedetailsSerializer
from . models import Contact,Educationdetail,Familydetails,Partnerprefarencedetails
from rest_framework import status
# Create your views here.

class Contact_API(APIView):
    def get(self,request,pk=None):
        if pk==None:
            obj=Contact.objects.all()
            serializer=ContactSerializer(obj,many=True)
            return Response(data=serializer.data)
        objs=get_object_or_404(Contact,id=pk)
        serializer=ContactSerializer(objs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data,status=status.HTTP_201_CREATED)
        return Response(data={"msg":"DATA IS INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        obj=Contact.objects.get(id=pk)
        serializer=ContactSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        obj=Contact.objects.get(id=pk)
        serializer=ContactSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        obj=get_object_or_404(Contact,id=pk)
        obj.delete()
        return Response(data={"msg":"DATA DELETED"},status=status.HTTP_200_OK)
    
class Educationdetail_API(APIView):
    def get(self,request,pk=None):
        if pk==None:
            obj=Educationdetail.objects.all()
            serializer=EducationdetailSerializer(obj,many=True)
            return Response(data=serializer.data)
        objs=get_object_or_404(Educationdetail,id=pk)
        serializer=EducationdetailSerializer(objs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=EducationdetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data,status=status.HTTP_201_CREATED)
        return Response(data={"msg":"DATA IS INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        obj=Educationdetail.objects.get(id=pk)
        serializer=EducationdetailSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        obj=Educationdetail.objects.get(id=pk)
        serializer=EducationdetailSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        obj=get_object_or_404(Educationdetail,id=pk)
        obj.delete()
        return Response(data={"msg":"DATA DELETED"},status=status.HTTP_200_OK)
    
class Familydetails_API(APIView):
    def get(self,request,pk=None):
        if pk==None:
            obj=Familydetails.objects.all()
            serializer=FamilydetailsSerializer(obj,many=True)
            return Response(data=serializer.data)
        objs=get_object_or_404(Familydetails,id=pk)
        serializer=FamilydetailsSerializer(objs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=FamilydetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data,status=status.HTTP_201_CREATED)
        return Response(data={"msg":"DATA IS INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        obj=Familydetails.objects.get(id=pk)
        serializer=FamilydetailsSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        obj=Familydetails.objects.get(id=pk)
        serializer=FamilydetailsSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        obj=get_object_or_404(Familydetails,id=pk)
        obj.delete()
        return Response(data={"msg":"DATA DELETED"},status=status.HTTP_200_OK)
    
class Partnerprefarencedetails_API(APIView):
    def get(self,request,pk=None):
        if pk==None:
            obj=Partnerprefarencedetails.objects.all()
            serializer=PartnerprefarencedetailsSerializer(obj,many=True)
            return Response(data=serializer.data)
        objs=get_object_or_404(Partnerprefarencedetails,id=pk)
        serializer=PartnerprefarencedetailsSerializer(objs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=PartnerprefarencedetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data,status=status.HTTP_201_CREATED)
        return Response(data={"msg":"DATA IS INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        obj=Partnerprefarencedetails.objects.get(id=pk)
        serializer=PartnerprefarencedetailsSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        obj=Partnerprefarencedetails.objects.get(id=pk)
        serializer=PartnerprefarencedetailsSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        obj=get_object_or_404(Partnerprefarencedetails,id=pk)
        obj.delete()
        return Response(data={"msg":"DATA DELETED"},status=status.HTTP_200_OK)