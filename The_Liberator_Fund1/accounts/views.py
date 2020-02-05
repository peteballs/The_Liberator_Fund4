from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib.auth import login as auth_login

User = get_user_model()

def register(request):
    if request.method == 'POST':
        new_user = User(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()

        print('SUBMITTED REG')
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def user_login(request):
    if request.method =='POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
    
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')
    
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
