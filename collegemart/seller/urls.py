from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns=[
    path('',views.productsale,name="saleform.home"),
    path('sale/',views.tosell,name="tosell")
]