from django.shortcuts import render

# Create your views here.
def membersView(request):
    return render(request, 'home/members.html',{})
   