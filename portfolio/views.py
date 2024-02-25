from django.shortcuts import render
from .models import Posts

def testimonial(request):
    posts = Posts.objects.all()
    return render(request, 'pages/testimonials.html', {'posts': posts})

