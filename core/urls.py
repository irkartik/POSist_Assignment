from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^createGenesisNode/', views.createGenesisNode),
    url(r'^createChildNode/', views.createChildNode),
    url(r'^editNode/', views.ediNode),  
]
