from django.urls import path
from django.contrib import admin
from Api_Login.views import RegisterView, LoginView,ProfileView, LogoutView, LogoutAllView

from Api_Admin.views import AddContactView,ListContactView
from Api_Admin.views import AddCategoryView, AddProductView, EditProductView,DeleteProductView

from Api_Home.views import AddCartView, CheckoutView,ContactInformationView
from Api_Home.views import ListCategoryView, ListProductView, ProductDetailView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)


urlpatterns = [

#### LOGIN PAGE ####
    path('', ProfileView.as_view()), 
    path('login/', LoginView.as_view()), 
    path('register/', RegisterView.as_view()),
    
### HOME PAGE ####
    path('list-category/', ListCategoryView.as_view()),
    path('list-product/', ListProductView.as_view()),
    path('detail-product/<int:pk>/', ProductDetailView.as_view()),
    path('add-cart/', AddCartView.as_view()),
    path('checkout/', CheckoutView.as_view()),
    path('contact-details/', ContactInformationView.as_view()),
    


#### ADMIN PAGE #####
# Contact Related Url
    path('add-contact/', AddContactView.as_view()),
    path('list-contact/', ListContactView.as_view()),
    
# Category Related Urls
    path('add-category/', AddCategoryView.as_view()),

# Product Related Urls
    path('add-product/', AddProductView.as_view()),
    path('edit-product/<int:pk>/', EditProductView.as_view()),
    path('delete-product/<int:pk>/', DeleteProductView.as_view()),


#### ADMIN PANNEL ####
    path('admin/', admin.site.urls),

# Token Related Urls
    path('token-generate/', TokenObtainPairView.as_view(), name='token-generate'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token-refresh/',TokenRefreshView.as_view(), name='token-refresh'),

    path('logout/',LogoutView.as_view()),
    path('logout-all/',LogoutAllView.as_view()),
]
