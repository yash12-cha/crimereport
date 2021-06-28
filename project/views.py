from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,logout
from django.contrib.auth import login as auth_login
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def about1(request):
    return render(request,'about1.html')
def contact1(request):
    return render(request,'contact1.html')
def sample(request):
    return render(request,'sample.html')
def login(request):
    return render(request,'login.html')
def report(request):
    return render(request,'report.html')
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

         # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Password mismatch!")
             return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, "Registered Successfully, Please Login...!")
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect("sample")


        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out.")
    return redirect('home')
