from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 photo = models.ImageField(upload_to='myimage')
 date = models.DateTimeField(auto_now_add=True)
 likes = models.ManyToManyField(User, related_name='post_liked')
 def __str__(self):
  return str(self.id)

 