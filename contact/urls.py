from django.urls import path
from .views import contact, about
urlpatterns = [
    path('contact/',contact, name='contact'),
    path('about/',about, name='about'),
]
