from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "readsapp/index.html")

def register(request):
    if request.method == "POST":
        errors = Users.objects.register_validator(request.POST)
        if len(errors) >0:
            for tags, value in errors.items():
                messages.error(request,value, extra_tags= tags)
            return redirect("/")
        else:
            name = request.POST["name"]
            alias = request.POST["alias"]
            email = request.POST["email"]
            password = request.POST["password"]
            hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            newuser = Users.objects.create(name= name, email= email, password= hash1.decode())
            request.session['user'] = newuser.name
            request.session['id'] = newuser.id
            return redirect("/books")

def login(request):
    if request.method == "POST": 
        errors = Users.objects.login_validator(request.POST)
        if len(errors) >0:
            for tags, value in errors.items():
                messages.error(request,value, extra_tags=tags)
            return redirect("/")
        else:
            current_user = Users.objects.filter(email= request.POST['lmail'])
            request.session['user'] = current_user.first().name
            request.session['id'] = current_user.first().id
            return redirect("/books")


def showbooks(request):
    context = {
        "reviews": Reviews.objects.all().order_by("-created_at"),
        "user" : Users.objects.get(id = request.session['id']) 
    }
    return render(request, "readsapp/books.html", context)

def addbook(request):
    context = { 
        'all_books': Books.objects.all()
    }
    return render(request, "readsapp/booksadd.html", context)

def addbookprocess(request):
        
    if request.method == "POST":
        if request.POST['newauthor'] & request.POST['author']:
            author= request.POST['newauthor']
        else:
            author= request.POST['author']
        newbook = Books.objects.create(title=request.POST['title'], author= author)
        newreview= request.POST['review']
        newrating= request.POST['rating']
        Reviews.objects.create(review=newreview, rating= newrating, users_who_reviewed= request.session['id'], books_reviewed=newbook)
        return redirect("/books") 
def logout(request):
    request.session.clear()
    return redirect("/")