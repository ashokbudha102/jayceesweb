from .views import membersView
from django.urls import path, include

urlpatterns = [
    path('members/<id>', membersView, name='members'),
]
