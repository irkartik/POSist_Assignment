from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^createGenesisNode/', views.createGenesisNode),
    url(r'^createChildNode/', views.createChildNode),
    url(r'^editNode/', views.ediNode),  
    url(r'^findLongestChain/', views.findLongestChain), 
]


'''
API ENDPOINTS

1. localhost:8000/createGenesisNode
2. localhost:8000/createChildNode
3. localhost:8000/editNode
4. localhost:8000/findLongestChain
'''