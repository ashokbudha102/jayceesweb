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
    thumbnail = models.ImageField(upload_to='post_thumbs')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = RichTextField()
    slug=models.SlugField(null=True, blank=True,editable=False)
    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            self.slug = slug
        super(Post,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogsingle', kwargs={'slug': self.slug})
