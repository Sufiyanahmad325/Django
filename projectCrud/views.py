from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, welcome to the Project home page!")
    return render(request , 'website/index.html')

def about(request):
    return render(request , 'website/about.html')


def contact(request):
    return render(request , 'website/contact.html')



def tech(request):
    return HttpResponse("Hello, welcome to the Project contact page!")