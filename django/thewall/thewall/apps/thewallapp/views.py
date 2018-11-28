from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "thewallapp/index.html")

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
            Users.objects.create(first_name= first_name, last_name=last_name, email=email, password=hash1.decode())
            request.session['user']= Users.objects.last().id 
            return redirect("/wall")
def login(request):
    if request.method == "POST": 
        errors = Users.objects.login_validator(request.POST)
        if len(errors) >0:
            for tags, value in errors.items():
                messages.error(request,value, extra_tags=tags)
            return redirect("/")
        else:
            request.session['user'] = Users.objects.filter(email= request.POST['lemail']).first().id
            return redirect("/wall")

def wall(request):
    if not 'key' in request.session: 
        return redirect("/")
    context ={
        "user": Users.objects.get(id=request.session['user']),
        "new_message": Messages.objects.all().order_by("-created_at"),
        
    }
    return render(request, "thewallapp/wall.html", context)

def msgprocess(request):
    errors = Messages.objects.message_validator(request.POST)
    if len(errors) > 0:
        for tags,value in errors.items():
            messages.error(request, value, extra_tags= tags)
        return redirect("/wall")
    if request.method == "POST":
        message = request.POST['mtext']
        user = request.session['user']
        current_user= Users.objects.get(id= user)
        Messages.objects.create(message = message, users_who_message= current_user)
        return redirect("/wall")

def cmtprocess(request, id):
    errors = Comments.objects.comment_validator(request.POST)
    if len(errors) > 0:
        for tags,value in errors.items():
            messages.error(request, value, extra_tags= tags)
        return redirect("/wall")
    if request.method == "POST":
        request.session['comment'] = request.POST['ctext']
        current_user= Users.objects.get(id= request.session['user'])
        comment = request.POST['ctext']
        message = Messages.objects.get(id=id)
        Comments.objects.create(comment= comment, message_with_comments= message, users_who_comments= current_user)
        print(Comments.objects.all())
        return redirect("/wall")
def logout(request):
    request.session.clear()
    return redirect("/")
