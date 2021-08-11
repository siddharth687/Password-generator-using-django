import generator
from django.shortcuts import render
import random
# Create your views here.
from django.http import HttpResponse

def home(request):
    print("Request is ----",request)
    return render(request,'generator/home.html')

def password(request):
    characters = list('')

    print('printing request-------',request.GET)

    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        #characters = (list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get("number"):
        characters.extend(list('1234567890'))
        #characters = (list('1234567890'))

    if request.GET.get("special"):
        characters.extend(list('!@#$%^&*()_-+=}{][:;.,><?/|'))
        #characters = (list('0123456789'))
        
    thepassword = ''
    length1 = int(request.GET.get('length'))

    for x in range(length1):
        thepassword += random.choice(characters)
    
    print("Request is ----",request)
    return render(request, "generator/password.html", {'password':thepassword})


def about(request):
    return render(request, 'generator/about.html')

def new(request):
    return render(request,'generator/new.html')