from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User


def home(request):
    return render(request, 'system/home.html')


def login(request):
    if request.method == "POST":
        user_id = request.POST.get('userId')
        password = request.POST.get('password')

        user = User.objects.filter(user_id=user_id, password=password)

        if len(user) != 0:
            messages.success(request, f"Logged in as {user_id}")
            params = {"user": user_id, "balance": user[0].balance}

            return render(request, 'system/user.html', params)

        else:
            messages.error(request, "Login failed. Please check your User ID and password")
            return redirect('Home')

    return HttpResponse("Error")


def create_account(request):
    if request.method == "POST":
        user_id = request.POST.get('userId')
        password = request.POST.get('password')

        user = User.objects.filter(user_id=user_id, password=password)
        print(user)

        if len(user) == 0:
            user = User.objects.create(user_id=user_id, password=password)
            messages.success(request, "Account created successfully")

            return redirect('Home')

        else:
            messages.error(request, "User ID already exists.")
            return redirect('Create Account')

    else:
        return render(request, 'system/create_account.html')


def transaction(request):
    if request.method == "POST":
        amount = int(request.POST.get('amount'))
        user_id = request.POST.get('user')
        action = request.POST.getlist('action')[0]

        print(action)

        user = User.objects.filter(user_id=user_id)
        balance = user[0].balance

        if action == "withdraw":
            print(1)
            if balance - amount >= 0:
                balance -= amount
                messages.success(request, f"Successfull withdrawal of Rs. {amount}")

            else:
                messages.error(request, "Balance not sufficient.")
                params = {"user": user_id, "balance": balance}
    
                return render(request, 'system/user.html', params)
                                
        else:
            balance += amount
            messages.success(request, f"Successfully deposited Rs. {amount}")


        User.objects.filter(user_id=user_id).update(balance=balance)

        params = {"user": user_id, "balance": balance}
        return render(request, 'system/user.html', params)
    
    return HttpResponse("Error")
