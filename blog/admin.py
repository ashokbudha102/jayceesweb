from django.contrib import admin
from .models import Author, Post, Comments
# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comments)