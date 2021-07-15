from django.shortcuts import render
from .models import membersRobo
# Create your views here.
def membersView(request):
    members=membersRobo.objects.all()
    context={'members':members}
    return render(request, 'members.html',context)