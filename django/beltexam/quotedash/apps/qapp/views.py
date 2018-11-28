from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "qapp/register.html")

def register(request):
    if request.method == "POST":
        errors = Users.objects.register_validator(request.POST)
        if len(errors) >0:
            for tags, value in errors.items():
                messages.error(request,value, extra_tags= tags)
            return redirect("/")
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pw']
        hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        Users.objects.create(first_name= first_name, last_name=last_name, email=email, password=hash1.decode())
        request.session['user']= Users.objects.last().id
        return redirect("/quotes")
def login(request):
    if request.method == "POST": 
        errors = Users.objects.login_validator(request.POST)
        if len(errors) >0:
            for tags, value in errors.items():
                messages.error(request,value, extra_tags=tags)
            return redirect("/")
        else:
            request.session['user'] = Users.objects.filter(email= request.POST['lemail']).first().id
            return redirect("/quotes")

def quotes(request):
    context= {
        "user": Users.objects.get(id=request.session['user']),
        "quotes": Quotes.objects.all(),
    }
    return render(request, "qapp/quotes.html", context)

def addquotes(request):
    if request.method == "POST":
        errors= Quotes.objects.quote_validator(request.POST)
        if len(errors) > 0:
            for tags, value in errors.items():
                messages.error(request,value, extra_tags=tags)
            return redirect("/quotes")
        else:
            quotes= request.POST['quote']
            author= request.POST['author']
            current_user = Users.objects.get(id = request.session['user'])
            Quotes.objects.create(quote= quotes, author= author, users_who_quote= current_user)
            return redirect("/quotes")

def showuser(request,id):
    current_user= Users.objects.get(id = id)
    context= {
        "userquotes": Quotes.objects.filter(users_who_quote= current_user),
        "user": current_user
    }
    return render(request, "qapp/showquotes.html", context)

def edituser(request,id):
    current_user= Users.objects.get(id = id)
    context={
        'user': current_user,
    }
    return render(request, "qapp/edituser.html", context)

def editprocess(request, id):
    if request.method == "POST":
        errors= Users.objects.edit_validator(request.POST)
        if len(errors)> 0 :
            for tags, value in errors.items():
                messages.error(request,value, extra_tags= tags)
            return redirect(f"/user/{id}")
        else:
            edituser= Users.objects.get(id= id)
            edituser.first_name = request.POST['fnedit']
            edituser.last_name= request.POST['lnedit']
            edituser.email= request.POST['emedit']
            edituser.save()
            return redirect("/quotes")

def deletequote(request, id):
    deletequote = Quotes.objects.get(id = id)
    deletequote.delete()
    return redirect("/quotes")

def likes(request, id):
    user = Users.objects.get(id = request.session['user'])
    quote = Quotes.objects.get(id= id)
    if len(Likes.objects.filter(quotes_with_likes = quote, user_who_likes= user)) > 0:
        return redirect("/quotes")
    else:
        Likes.objects.create(quotes_with_likes= quote, user_who_likes= user)
        return redirect("/quotes")
def logout(request):
    request.session.clear()
    return redirect("/")