from Api_Admin.models import Category, Product, Contact
from Api_Home.models import Cartlist,Items,Checkout

from django_filters import FilterSet, RangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ListCatergorySerializer, ListProductSerializer, ProductDetailSerializer
from .serializers import AddCartSerializer, CheckoutSerilaiser, ContactInformationSerialiser

# List Category View
class ListCategoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = ListCatergorySerializer


# Pric Filter Class
class PriceFilter(FilterSet):
    price = RangeFilter()
    class Meta:
        model = Product
        fields = ['price']

# List Product View
class ListProductView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_class = PriceFilter
    search_fields = ['category__category_name','product_name',]


# Product Detail View
class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

# Add to Cart
class AddCartView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset =  Items.objects.all()
    serializer_class = AddCartSerializer

# Contact information View
class ContactInformationView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactInformationSerialiser

class CheckoutView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerilaiser
