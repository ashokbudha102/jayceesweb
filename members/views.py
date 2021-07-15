from django.shortcuts import render
from .models import membersRobo
# Create your views here.
def membersView(request, id):
    members = membersRobo.objects.filter(yearMembership__id=id)
    context={'members':members}
    return render(request, 'members.html',context)
