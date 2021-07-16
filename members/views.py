from django.shortcuts import render
from .models import membersRobo, yearTeam
# Create your views here.
def membersView(request, id):
    members = sorted(membersRobo.objects.filter(yearMembership__id=id),key=lambda t: t.ordering)
    context={'members':members}
    return render(request, 'members.html',context)

def yearview(request):
    years=yearTeam.objects.all()
    return render(request, 'yearteam.html',{'years':years})
