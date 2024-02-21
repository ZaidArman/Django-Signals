from django.shortcuts import render, redirect
from .forms import SignUp, Login
from django.contrib import messages
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Post
# Create your views here.

my_signals = Signal()

def index(request):
    return render(request, 'login.html')

def signup(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            Login(request, user)
            return redirect('login')  # Redirect to your home page or any other desired page
    return render(request, 'signup.html', {'form': form})

# @receiver(request_finished)
# def func(sender, **kwargs):
#     print("Request Finished ")
    
# @receiver(my_signals)
# def func2(sender, **kwargs):
#     print(" \n\n ", kwargs)