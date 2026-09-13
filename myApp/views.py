from django.shortcuts import render
from .models import chaiVerity # yeha pe hamne chaiVerity model ko import kiya hai taki ham usko views me use kar sakein
from django.shortcuts import get_object_or_404 # yeha pe hamne get_object_or_404 function ko import kiya hai taki ham usko views me use kar sakein

# Create your views here.

def all_chai(request):
    chais = chaiVerity.objects.all() # yeha pe hamne chaiVerity model ka use karke sabhi chai ke objects ko fetch kiya hai aur unko chais variable me store kiya hai
    return render(request, 'myApp/all_chai.html', {'chais': chais} ) # yeha pe hamne render function ka use karke all_chai.html template ko render kiya hai aur chais variable ko template me pass kiya hai taki ham template me sabhi chai ke objects ko access kar sakein

def order(request):
    return render(request, 'myApp/order.html')


def chai_detail(request , chai_id):
    chai = get_object_or_404(chaiVerity, id=chai_id) # yeha pe hamne chaiVerity model ka use karke chai_id ke basis pe chai ke object ko fetch kiya hai aur unko chai variable me store kiya hai
    return render(request, 'myApp/chai_details.html', {'chai': chai}) # yeha pe hamne render function ka use karke chai_detail.html template ko render kiya hai aur chai variable ko template me pass kiya hai taki ham template me chai ke object ko access kar sakein

