from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def numgen(request):
    if 'key' in request.session:
        request.session["key"] += 1
        
    else:
        request.session["key"] = 0
    randomstring = {
        "string":get_random_string(length=14)
    }
    return render(request,"index.html", randomstring)
def delete(request):
    del request.session['key']
    return redirect("/")
# Create your views here.
