from django.urls import path, include
from .views import blogindex, blogsingle
urlpatterns = [
    path('',blogindex,name='blogindex'),
    path('blog/<slug:slug>',blogsingle,name='blogsingle'),
]
