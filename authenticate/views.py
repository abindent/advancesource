from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

# Auth
def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['user_name']
        email = request.POST['email']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        pass1 = request.POST['user_password']
        pass2 = request.POST['confirm_password']

        # check for errorneous input
        if len(username) < 5:
            messages.error(
                request, " Your user name must be under 5 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('/')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, " Your AdvanceSource account has been successfully created")
        return redirect('/')

    else:
        return redirect("/")

def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
         
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return redirect("/")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
