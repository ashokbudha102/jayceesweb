from django.shortcuts import render, get_object_or_404
from .models import Post, Author,Comments
from .forms import commentForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def blogindex(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'queryset':paginator_queryset,'page_request_var':page_request_var,'posts':posts})

def blogsingle(request,slug):
    news=get_object_or_404(Post,slug=slug)
    form=commentForm(request.POST or None)
    comments=Comments.objects.filter(post=news)
    if request.method=='POST':
        if form.is_valid:
            form.instance.news=news
            form.save()
            form=commentForm()
            return HttpResponseRedirect(request.path_info)
    return render(request, 'blog.html',{'news':news,'form':form})
