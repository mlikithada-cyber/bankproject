from .views import signup, login_user, verify_otp
from django.urls import path

urlpatterns = [
   
    path('signup/',signup,name='signup'),
    path('login/',login_user,name='login_user'),
    path('otp/',verify_otp,name='otp')

]