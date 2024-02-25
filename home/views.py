from django.shortcuts import render, HttpResponse, redirect
from .models import *

def home(request):
    return render(request,'pages/index.html')
    
    
def termsCondition(request):
    return render(request,'pages/index.html')
    
def privacyPolicy(request):
    return render(request,'pages/index.html')
    
def subscription(request):
    if request.method=='POST':
   	 subscriptionemail = request.POST['subscriptionemail']
   	 
   	 subscription = Subscription(subscriptionemail=subscriptionemail)
   	 subscription.save()
    return redirect('home')
