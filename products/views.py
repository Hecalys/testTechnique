from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
import datetime


from .models import Product

def index(request):
    if request.method == 'POST': 
        update_given_gtin = request.POST['update_given_gtin']
        expiration_date = request.POST['expiration_date']
        if Product.objects.filter(product_gtin = update_given_gtin).count() > 0:
            Product.objects.filter(product_gtin = update_given_gtin).update(exp_date = expiration_date)
        else:
            Product(product_gtin = update_given_gtin, exp_date = expiration_date).save()
    latest_product_list = Product.objects.order_by('product_gtin')
    context = {'latest_product_list': latest_product_list}
    return render(request, 'products/index.html', context)
    

def plist(request):
    product_list = Product.objects.order_by('exp_date')
    return render(request, 'products/plist.html', {'product_list': product_list})