from django.shortcuts import render

# Create your views here.

def all_chai(request):
    return render(request, 'myApp/all_chai.html')

def order(request):
    return render(request, 'myApp/order.html')