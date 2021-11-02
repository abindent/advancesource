from django.shortcuts import render, redirect
from home.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
# Create your views here.

def index(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')    

def game(request):
    return render(request, 'homepage/game.html')    

@login_required(login_url="/login")
def contact(request):
  if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact= Contact(user=request.user,name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
  return render(request, "homepage/contact.html")
