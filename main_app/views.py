from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import (Book, Genre, UserBook, Comments)

# Create your views here.
def index(request):
    
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect('admin/')
        else:
            return HttpResponseRedirect('user/')
    else:
        return HttpResponseRedirect('accounts/login/')


def registration(request):

    return render(request, 'registration/registration.html')

def guest(request):

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'guest.html', context)

def user_home(request):

    pass

def admin_home(request):

    pass

def sign_up(request):

    email = request.POST['email']
    password = request.POST['password']
    password_check = request.POST['password_check']

    if password == password_check:
        try:
            user = User.objects.create_user(email, email, password)
        except:
            return HttpResponse('User already exist.')
    
    return HttpResponse('Success!')

def log_in(request):

    username = request.POST['email']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Wrong login or password')