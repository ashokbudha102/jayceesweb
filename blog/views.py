from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def blogindex(request):
    posts=Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 6)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': blogs})

def blogsingle(request,slug):
    news=get_object_or_404(Post,slug=slug)
    return render(request, 'blog.html',{'blog':news})
