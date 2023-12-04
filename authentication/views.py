from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:#if valid user, redirect to home page
            login(request, user)
            return redirect('index')
        else:#else, redirect to home page
            messages.success(request, ("There was an error logging in, Try Again!"))
            return redirect('login')
    else:
        return render(request, 'Registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('index')


def register_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, 'Registration/register.html', {"form": form})
