from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


def Create_Account(request):
    return render(request,'account.html')
def Checkout(request):
    return render(request, 'checkout.html')

def Trackker(request):
    return render(request, 'trackker.html')
