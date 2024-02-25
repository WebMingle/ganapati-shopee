from django.shortcuts import render, HttpResponse

def service(request):
    return render(request,'pages/service.html')
