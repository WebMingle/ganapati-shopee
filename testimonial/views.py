from django.shortcuts import render
from .models import Post

def testimonial(request):
    posts = Post.objects.all()
    return render(request, 'pages/testimonials.html', {'posts': posts})

