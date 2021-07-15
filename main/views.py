from django.shortcuts import render
from blog.models import Post
# Create your views here.

def home_view(request):
    objects=Post.objects.all().order_by('-id')[0:3]
    return render(request,'main/home.html', {'objects':objects})



