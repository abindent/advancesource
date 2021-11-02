from django.shortcuts import render, redirect

# Create your views here.

#Normal
def userlogin(request):
    return render(request, "authentication/account/login.html")

def usersignup(request):
    return render(request, "authentication/account/register.html")    


      