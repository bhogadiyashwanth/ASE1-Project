from django.shortcuts import render
from . models import Products_Selling
from registration.models import Profile
from . forms import saleform
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def productsale(request):
    if request.method == 'POST':
        form3=saleform(request.POST, request.FILES)
        if form3.is_valid():
            product = form3.save()
            p = Profile.objects.get(user=request.user)
            product.Seller.add(p)
            print(product)
            product.save()
            return HttpResponse(product)
    else:
        form3 = saleform()
        return render(request, 'seller/saleform.html', {'form3': form3})

@login_required()
def tosell(request):
    p = Profile.objects.get(user=request.user)
    m = Products_Selling.objects.filter(Seller=p)
    return render(request, 'seller/tosell.html', {'m':m})

