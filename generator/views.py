# generator app
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')
    


def passwordGenerator(request):
    
    char = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('symbols'):
        char.extend(list('!@#$%^&*()'))
        
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))
        
        
    length = int(request.GET.get('length'))
    
    password  = ''
    for x in range(length):
        password += random.choice(char)
        
        
    return render(request, 'result.html', {'password':password})
        
        
        
    
        
    