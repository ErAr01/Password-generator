from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abedefghijklmnoparstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPORSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){}[]`~\|/?><'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for r in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : thepassword})

def info(request):
    return render(request, 'generator/info.html')

# Create your views here.
