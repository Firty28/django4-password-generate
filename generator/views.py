from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    deska = {'username':['egorka', 'Egor2006!', 'Mamama', 'qwerty']}
    return render(request, 'generator/index.html', deska) 


def password(request):
    character = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        character.extend(list('QAZWSXEDCRFVTGBYHNUJMIKOLP'))

    if request.GET.get('numbers'):
        character.extend(list('0123456789'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_+'))

    lenght = int(request.GET.get('lenght', 12))

    the_password = ''

    for x in range(lenght):
        the_password += random.choice(character)


    return render(request, 'generator/password.html', {'password':the_password})
    


def author(request):
    return render(request, 'generator/authot.html')