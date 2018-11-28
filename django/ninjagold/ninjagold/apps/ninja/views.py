from django.shortcuts import render, redirect 
import random
def index(request):
    if 'key' in request.session:
        pass
        
    else:
        request.session["key"] = 0
        request.session["gold"] = 0
        request.session["earned"]= 0
    request.session["gold"] += request.session["earned"]
    request.session["earned"] = 0
    goldamount = {
        'gold' : request.session['gold']
    }
        
    return render(request, "index.html", goldamount)
def process(request,name):
    makegold = {
        'farm': random.randint(10,20),
        'cave': random.randint(5,10),
        'house': random.randint(2,5),
        'casino': random.randint(-51,51)
    }
    request.session["earned"] = makegold[name]
    return redirect('/')

# Create your views here.
