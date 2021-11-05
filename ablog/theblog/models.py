from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    header_image = models.ImageField(null = True, blank = True, upload_to= "images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='uncategorized')
    snippet = models.CharField(max_length=255, default='Click link above to read...')
    body = RichTextField(blank = True, null = True)
    # body = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class EditPost(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255, default='Click link above to read...')
    body = models.TextField()
    header_image = models.ImageField(null = True, blank = True, upload_to= "images/")


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
        


