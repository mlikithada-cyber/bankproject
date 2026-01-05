
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
              
    path('admin/', admin.site.urls),
    path('deposits/', include('deposits.urls')),
    path('', include('home.urls')),  
    path('account_open/', include('users.urls')),    
    path('user_accounts/', include('user_accounts.urls')),  
    
]