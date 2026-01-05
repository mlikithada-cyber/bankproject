from django.shortcuts import render
from .models import User_Accounts

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("psw")
        confirm_password = request.POST.get("psw-repeat")

        # 1️⃣ Password match check
        if password != confirm_password:
            return render(request, 'user_accounts/signup.html', {
                'error': 'Passwords do not match'
            })

        # 2️⃣ Duplicate email check
        if User_Accounts.objects.filter(email=email).exists():
            return render(request, 'user_accounts/signup.html', {
                'error': 'Email already registered'
            })

        # 3️⃣ Save to YOUR custom table
        User_Accounts.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password   # ⚠️ plain text (see note below)
        )

        return render(request, 'user_accounts/signup.html', {
            'success': 'Account created successfully'
        })

    return render(request, 'user_accounts/signup.html')

def login_user(request):
    error = ""
    success = ""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("psw")

        try:
            user = User_Accounts.objects.get(email=email, password=password)
            success = f"Login successful. Welcome {user.first_name}"
            print("LOGIN SUCCESS:", email)
        except User_Accounts.DoesNotExist:
            error = "Invalid email or password"
            print("LOGIN FAILED:", email)

    return render(request, "user_accounts/login.html", {
        "error": error,
        "success": success
    })