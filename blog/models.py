from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.text import slugify


User=get_user_model()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='post_thumbs')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    content = RichTextField()
    slug=models.SlugField(null=True, blank=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogsingle', kwargs={'slug': self.slug})
    
    @property
    def comments(self):
        return self.comment.all().order_by('-timestamp')


class Comments(models.Model):
    content=models.TextField()
    name=models.CharField(max_length=100)
    email=models.EmailField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return self.name
        
