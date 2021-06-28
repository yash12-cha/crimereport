from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from crime.models import Reports
from crime.models import Report
from crime.models import extendeduser
from django.contrib.auth  import authenticate,logout
from django.contrib.auth import login as auth_login
def dashboard(request):
    return render(request,'dashboard.html')
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
def my_complaints(request):
    log_user = request.user
    complaints = Report.objects.filter(user1 = log_user)
    return render(request,'my_complaints.html',{'complaints' : complaints})

def report(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        complaint_title=request.POST['complaint_title']
        incident=request.POST['incident']
        content=request.POST['content']
        happen =request.POST['happen']
        date =request.POST['date']
        report=Report(name=name, email=email, phone=phone,title=complaint_title, category=incident, complain=content, place=happen,date=date,user1=request.user)
        report.save()
        messages.success(request, "Complaint Filed Successfully. One of our executives will get back to you shortly....!")
    return render(request,'report.html')
def handleSignUp(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        Phone=request.POST['Phone']
        dob=request.POST['dob']
        address=request.POST['address']

        if (pass1 == pass2):
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already taken.Please try again")
                return redirect('home')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email Already Registered.Please try again")
                return redirect('home')
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name= fname
                myuser.last_name= lname
                myuser.save()
                yash = extendeduser(phone_num =Phone,addre=address,dob=dob,user=myuser)
                yash.save()
                messages.success(request, "Registered Successfully, Please Login...!")
                return redirect('home')

        else:
            messages.error(request, "Password mismatch.Please try again")
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
