from django import forms
from . models import Products_Selling

class saleform(forms.ModelForm):


    class Meta:
        model = Products_Selling
        fields = ('pname', 'description','photo','Category', 'amount')

