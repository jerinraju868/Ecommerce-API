from django.shortcuts import render
from Api_Admin.models import Contact, Category, Product
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import AddContactSerializer, ListContactSerializer
from .serializers import AddCatergorySerializer, AddProductSerializer, EditProductSerializer,DeleteSerializer

# Add Contact information view
class AddContactView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contact.objects.all()
    serializer_class = AddContactSerializer

# List Contact information view 
class ListContactView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contact.objects.all()
    serializer_class = ListContactSerializer

# Add Category View
class AddCategoryView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = AddCatergorySerializer

# Add Product View
class AddProductView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

# Edit Product View
class EditProductView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = EditProductSerializer

# Delete Product View
class DeleteProductView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = DeleteSerializer