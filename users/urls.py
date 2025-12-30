from .views import open_account
from django.urls import path
urlpatterns = [
    path('',open_account,name='open_account')
]