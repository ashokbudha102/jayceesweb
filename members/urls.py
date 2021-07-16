from .views import membersView, yearview
from django.urls import path, include

urlpatterns = [
    path('members/<id>', membersView, name='members'),
    path('yearteam/', yearview, name='year'),
]
