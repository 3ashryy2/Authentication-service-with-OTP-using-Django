from django.urls import path
from .views import change_password, register_user, user_login, user_logout, LoginWithOTP, ValidateOTP


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('login-with-otp/', LoginWithOTP.as_view(), name='login-with-otp'),
    path('validate-otp/', ValidateOTP.as_view(), name='validate-otp'),
    path('change_password/', change_password, name='change_password'),
]
