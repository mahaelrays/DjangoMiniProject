from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.timezone import now

# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title

    def get_absolute_url(self):
        return redirect('home')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, related_name='comments',on_delete=models.CASCADE) 
    #blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content

