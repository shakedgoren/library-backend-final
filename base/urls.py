from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('books/', views.BookView.as_view()),
    path('books/<id>', views.BookView.as_view()),
    path('clients/', views.ClientView.as_view()),
    path('clients/<id>', views.ClientView.as_view()),
    path('loans/', views.LoanView.as_view()),
    path('loans/<id>', views.LoanView.as_view()),
   ]

