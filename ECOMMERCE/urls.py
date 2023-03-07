from django.urls import path
from django.contrib import admin
from Api_Login.views import RegisterView, LoginView,ProfileView
from Api_Admin.views import AddContactView,ListContactView
from Api_Admin.views import AddCategoryView, ListCategoryView, AddProductView, ListProductView, EditProductView,DeleteProductView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)


urlpatterns = [
    path('', ProfileView.as_view()), 
    path('login/', LoginView.as_view()), 
    path('register/', RegisterView.as_view()),
    
#### ADMIN PAGE #####
# Contact Related Url
    path('add-contact/', AddContactView.as_view()),
    path('list-contact/', ListContactView.as_view()),
    
# Category Related Urls
    path('add-category/', AddCategoryView.as_view()),
    path('list-category/', ListCategoryView.as_view()),

# Product Related Urls
    path('add-product/', AddProductView.as_view()),
    path('list-product/', ListProductView.as_view()),
    path('edit-product/<int:pk>/', EditProductView.as_view()),
    path('delete-product/<int:pk>/', DeleteProductView.as_view()),


#### ADMIN PANNEL ####
    path('admin/', admin.site.urls),

# Token Related Urls
    path('token-generate/', TokenObtainPairView.as_view(), name='token-generate'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token-refresh/',TokenRefreshView.as_view(), name='token-refresh'),


]
