from django.shortcuts import render
from .models import gallery_images
# Create your views here.
def gallery(request):
    images = gallery_images.objects.all().order_by('-id')
    return render(request,'gallery.html',{'gallery':images})