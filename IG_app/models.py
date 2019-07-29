from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profiles(models.Model):
    image = models.ImageField(blank=True, )
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    def save_profile(self):
        self.save()
        
    @classmethod
    def get_profile_by_name(cls, name):
        profile = Profiles.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profiles.objects.filter(user = id).first()
        return profile
    
    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profiles.objects.get(user = id)
        return profile
    
class Images(models.Model):
    image = models.ImageField(blank=True, )
    caption = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-posted',)
        
    def save_image(self):
        self.save()
      
    @classmethod  
    def get_image_by_id(cls,id):
        image = Images.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls,profile):
        images = Images.objects.filter(profile__pk= profile)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = Images.objects.all()
        return images
    
class Comments(models.Model):
    comment = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Images,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def save_comment(self):
        self.save()
        
    @classmethod
    def get_comment_by_image(cls,id):
        comment = Comments.objects.filter(image__pk = id)
        return comment