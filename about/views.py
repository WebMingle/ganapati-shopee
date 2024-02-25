from django.shortcuts import render
from .models import Member

def about(request):
    members = Member.objects.all()
    return render(request, 'pages/about.html', {'members': members})

