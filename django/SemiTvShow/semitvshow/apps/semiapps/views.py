from django.shortcuts import render, HttpResponse, redirect
from .models import Shows
from django.contrib import messages

def addnewshows(request):
    return render(request,"semiapps/index.html")

def createprocess(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
    else:
        Shows.objects.create(title=request.POST['title'], network= request.POST['network'], release_date= request.POST['date'], desc=request.POST['desc']) 
        newshow= Shows.objects.last().id
        return redirect(f"/shows/{newshow}")

def showing(request, id):
    context={
        "tvshow": Shows.objects.get(id=id)  
    }
    return render(request,"semiapps/showshows.html", context)

def edit(request, id):
    context={
        "currentshow": Shows.objects.get(id=id),
        "date": Shows.objects.get(id=id).release_date.strftime("%Y-%m-%d")
    }
    return render(request,"semiapps/editshow.html", context)

def updateprocess(request, id):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) >0:
        for key, value, in errors.items():
            messages.error(request,value)
        return redirect(f"/shows/{id}/edit")
    else:
        show_to_update = Shows.objects.get(id=id)
        show_to_update.title= request.POST['title']
        show_to_update.network= request.POST['network']
        show_to_update.release_date= request.POST['date']
        show_to_update.desc= request.POST['desc']
        show_to_update.save()
        return redirect(f"shows/{id}")

def show(request):
    context={
        "all_shows": Shows.objects.all()
    }
    return render(request,"semiapps/shows.html", context)

def delete(request, id):
    show_to_delete = Shows.objects.get(id=id)
    show_to_delete.delete()
    return redirect(F"/shows")