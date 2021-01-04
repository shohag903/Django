from django.shortcuts import render, resolve_url

from django.http import HttpResponse


def home(request):
       return render(request,'index.html')

def about(request):
       return render(request,'about.html')

def contact(request):
       return render(request,'contact.html')


def help(request):
       return render(request,'help.html')