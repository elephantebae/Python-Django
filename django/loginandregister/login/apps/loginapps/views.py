from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "loginapps/index.html")

def register(request):
    if request.method == "POST":
        errors = Users.objects.register_validator(request.POST)
        if len(errors) >0:
            for tags, value in errors.items():
                messages.error(request,value, extra_tags= tags)
            return redirect("/")
        else:
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            email = request.POST['email']
            password = request.POST['pw']
            hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = Users.objects.create(first_name= first_name, last_name=last_name, email=email, password=hash1.decode())
            request.session['user']= user.id 
            return redirect("/success")
def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors) >0:
        for tags, value in errors.items():
            messages.error(request,value, extra_tags=tags)
        return redirect("/")
    else:
        if request.method == "POST": 
            request.session['user'] = Users.objects.filter(email= request.POST['lemail']).first().id
            return redirect("/success")

def success(request):
    context ={
        "user": Users.objects.get(id=request.session['user'])
    }
    return render(request, "loginapps/success.html", context)

