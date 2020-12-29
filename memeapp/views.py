from django.shortcuts import render , redirect , get_object_or_404 
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group , User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CreateUserForm
from .models import Customer 
from .service import get_memes
import json 

# Create your views here.
def homePage(request):
    context = {}
    cookie = False
    user = request.user
    if request.method == "GET":
        if user.is_authenticated:
            customer = Customer.objects.get(user=request.user)
            if customer.cookie:
                cookie = True
            context['customer'] = customer
        context['cookie'] = cookie
        return render(request,'memeapp/home.html',context)
    elif request.method == "POST":
        try:
            # update consent 
            context['redirect'] = '/memes'
            customer = Customer.objects.get(user=user)
            customer.cookie = True
            customer.save()
            return JsonResponse(context , status=200)
        except :
            context['error'] = 'Some error occured please try again'
            return JsonResponse(context , status=400)

def loginPage(request):
    context = {}
    if request.method == "GET":
        return render(request,'memeapp/login.html',context)
    elif request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=username, password=pwd)
        if user is not None :
            login(request,user)
            if user.is_authenticated and user.is_staff:
                return redirect('homePage')
            elif user.is_authenticated :
                return redirect('homePage')

        elif username is not None and pwd is not None:
            context = {'errorMessages' : 'username or password invalid'}
        return render(request,'memeapp/login.html' , context )
        

def registerPage(request):
    context = {}
    if request.method == 'GET':
        return render(request,'memeapp/register.html' , context )
    elif request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            userSigned = form.save(commit=True)
            username = form.cleaned_data['username']
            customer = Customer()
            customer.user = userSigned
            customer.save()
            messages.success(request,'Account created for ' + username)
            return redirect('loginPage')
        else:
            context = {'form' : form}
            return render(request,'memeapp/register.html' , context )

@login_required(login_url='loginPage')
def logoutPage(request):
    logout(request)
    return redirect('homePage')

def memePage(request):
    context = {}
    if request.method == "GET":
        memes = get_memes()
        if memes['success'] :
            data = memes['data']
            paginator = Paginator(data['memes'], 5)
            page = request.GET.get('page', 1)
            try:
                memes = paginator.page(page)
            except PageNotAnInteger:
                memes = paginator.page(1)
            except EmptyPage:
                memes = paginator.page(paginator.num_pages)
            context['memes'] = memes
        return render(request,'memeapp/memepage.html',context)
         

