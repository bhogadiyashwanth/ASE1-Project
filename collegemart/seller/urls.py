from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^productselling/$', views.productselling, name='productselling'),
    url(r'^productselling/confirmation/$', views.conf, name='conf'),
]
