from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tags(models.Model):
    name=models.CharField(max_length=20)
    
   

class Image(models.Model):
    image=models.ImageField(upload_to='/picture',)
    name=models.CharField(max_length=40)
    caption=models.CharField(max_length=25)
    profile=models.ForeignKey(User,on_delete=models.CASCADE,related_name="images",blank=True)
    likes=models.IntegerField(default=0)
    comments=models.TextField()
    tags=models.ManyToManyField(tags)
    location=models.ForeignKey(Location,null=True)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()