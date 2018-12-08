from django.shortcuts import render,redirect
from . models import ProductDetails
from django.http import HttpResponse
from django.contrib.auth.models import User

def productselling(request):
        return render (request, 'sales/productselling.html')
def conf(request):
    if request.method=='POST':
        prod_name = request.POST['prod_name']
        prod_description = request.POST['prod_description']
        image = request.POST['image']
        prod_type = request.POST['prod_type']
        amount = request.POST['amount']
        user = User.objects.get(pk=userid)
        ProductDetails.objects.create(prod_name=prod_name, prod_description=prod_description , image=image, prod_type=prod_type, amount=amount, user=user)
    return HttpResponse('It Worked!')