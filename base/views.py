from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Book,Client,Loan
from .serializer import MyTokenObtainPairSerializer,BookSerializer,ClientSerializer,LoanSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")

@permission_classes([IsAuthenticated])
class BookView(APIView):
    def get(self,request):
        my_model = Book.objects.all()
        serializer = BookSerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        my_model = Book.objects.get(id=id)
        serializer = BookSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = Book.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class ClientView(APIView):
    def get(self,request):
        my_model = Client.objects.all()
        serializer = ClientSerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        my_model = Client.objects.get(id=id)
        serializer = ClientSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = Client.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class LoanView(APIView):
    def get(self,request):
        allLoans = LoanSerializer(Loan.objects.all(),many=True).data
        for loan in allLoans:
            loan['clientID'] = {"name":Loan.objects.get(id=loan['id']).clientID.clientName,"id":Loan.objects.get(id=loan['id']).clientID.id}
            loan['bookID'] =  {"name":Loan.objects.get(id=loan['id']).bookID.bookName,"id":Loan.objects.get(id=loan['id']).bookID.id,"type":Loan.objects.get(id=loan['id']).bookID.bookType}
        return Response(allLoans)
    def post(self,request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        my_model = Loan.objects.get(id=id)

        serializer = LoanSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = Loan.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)