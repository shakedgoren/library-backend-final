from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Book,Client,Loan

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    def create(self, validated_data):
        return Client.objects.create(**validated_data)

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   @classmethod
   def get_token(cls, user):
       token = super().get_token(user)
       token['username'] = user.username
       token['email'] = user.email

       return token