from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There Was An Error Logging In, Try Again...")
            return redirect('loggin')
    else:
        return render(request, 'members/login.html', {})
def logout_user(request):
    logout(request)
    return redirect('index')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'members/register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            #messages.success(request, 'You have singed up successfully.')
            #login(request, user)
            return redirect('index')
        else:
            #print(form.errors)
            return render(request, 'members/register.html', {'form': form})