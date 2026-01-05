from .views import signup, login_user
from django.urls import path

urlpatterns = [
   
    path('signup/',signup,name='signup'),
    path('login/',login_user,name='login_user'),
]