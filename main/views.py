from django.shortcuts import render
from blog.models import Post
from  members.models import yearTeam
# Create your views here.

def home_view(request):
    objects=Post.objects.all().order_by('-id')[0:3]
    years=yearTeam.objects.all()
    return render(request,'main/home.html', {'objects':objects,'years':years})



