from .views import home_view,event_view
from django.urls import path, include

urlpatterns = [
    path('home/', home_view, name='home'),
    path('event/',event_view,name='events'),
]
