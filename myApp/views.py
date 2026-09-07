from django.shortcuts import render
from .models import chaiVerity # yeha pe hamne chaiVerity model ko import kiya hai taki ham usko views me use kar sakein

# Create your views here.

def all_chai(request):
    chais = chaiVerity.objects.all() # yeha pe hamne chaiVerity model ka use karke sabhi chai ke objects ko fetch kiya hai aur unko chais variable me store kiya hai
    return render(request, 'myApp/all_chai.html', {'chais': chais} ) # yeha pe hamne render function ka use karke all_chai.html template ko render kiya hai aur chais variable ko template me pass kiya hai taki ham template me sabhi chai ke objects ko access kar sakein

def order(request):
    return render(request, 'myApp/order.html')

