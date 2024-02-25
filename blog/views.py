from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all()

    # Number of posts per page
    posts_per_page = 15

    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'pages/blog.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {'post': post}
    return render(request, 'pages/blog-details.html', context)

