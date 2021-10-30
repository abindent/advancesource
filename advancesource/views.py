from django.shortcuts import render, redirect

def index(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')    