from .views import home_view,event_view
from django.urls import path, include

urlpatterns = [
    path('event/',event_view,name='events'),
    path('', home_view, name='home'),
]
