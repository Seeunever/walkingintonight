from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def create_pl(request):
    return render(request,'create_pl.html')

def back_to_index(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def choose_age_sex(request):
    return render(request,'choose_age_sex.html')

def choose_name(request):
    return render(request,'choose_name.html')