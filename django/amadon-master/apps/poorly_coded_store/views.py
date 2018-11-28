from django.shortcuts import render, redirect, HttpResponse
from .models import Order, Product
import decimal

def index(request):
    context = {
        "all_products": Product.objects.all(),
        "wired": Product.objects.first().price
    }

    if 'allpurchases' in request.session:
        pass
    else:
        request.session['allpurchases'] = 0
        request.session['quantity'] = 0
    return render(request, "store/index.html", context)

def checkoutprocess(request):
    if request.method == "POST":
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = Product.objects.first().price
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        request.session['quantity']+= float(Order.objects.last().quantity_ordered)    
        request.session['allpurchases'] += float(Order.objects.last().total_price)
        return redirect("/checkout")
    else:
        return redirect("/")

def checkout(request): 
    return render(request, "store/checkout.html")
    
        