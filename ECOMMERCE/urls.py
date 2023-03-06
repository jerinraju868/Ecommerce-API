from django.urls import path
from django.contrib import admin
from Api_Login.views import RegisterView, LoginView,ProfileView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)


urlpatterns = [
    path('', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('register/', RegisterView.as_view()),
    path('admin/', admin.site.urls),


    path('token-generate/', TokenObtainPairView.as_view(), name='token-generate'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token-refresh/',TokenRefreshView.as_view(), name='token-refresh'),


]
