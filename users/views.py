from django.shortcuts import render

def open_account(request):
    return render(request, 'users/account_open.html')