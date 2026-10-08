from urllib import request

from django.shortcuts import render, redirect
from.models import Logininfo,JobSeeker, Enquiry
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        contactno=request.POST.get("contactno")
        emailaddress=request.POST.get("emailaddress")
        enquirytext=request.POST.get("enquirytext")
        posteddate=datetime.datetime.today().strftime("%d/%m/%Y")
        enq=Enquiry(name=name, contactno=contactno, emailaddress=emailaddress, enquirytext=enquirytext, posteddate=posteddate)
        enq.save()
        messages.success(request, "Enquiry is saved successfully")
        return redirect('contact')
    return render(request, "contact.html")
def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        gender=request.POST.get("gender")
        contactno=request.POST.get("contactno")
        emailaddress=request.POST.get("emailaddress")
        qualification=request.POST.get("qualification")
        experience=request.POST.get("experience")
        keyskill=request.POST.get("keyskill")
        address=request.POST.get("address")
        password=request.POST.get("password")
        js=JobSeeker(name=name,gender=gender, contactno=contactno, emailaddress=emailaddress, qualification=qualification, experience=experience, keyskill=keyskill, address=address)
        li=Logininfo(uertype="jobseeker", username=emailaddress, password=password)
        js.save()
        li.save()
        messages.success(request, "registration is done")
        return redirect("register")
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")

        try:
            user = Logininfo.objects.get(username=username , password=password)
            if user is not None:
                if user.uertype == 'admin':
                    messages.success(request, "Welcome Admin")
                    request.session['adminid']=user.username
                    return redirect("admindash")
                elif user.uertype == 'jobseeker':
                    messages.success(request, "Welcome jobseeker")
                    request.session['userid']=user.username
                    return redirect("userdash")
        except Logininfo.DoesNotExist:
                messages.error(request, "Invalid username or password")
                return redirect("login")
    return render(request, "login.html")

        
