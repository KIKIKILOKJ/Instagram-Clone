from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tags(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name()
    
    def save_tags(self):
        self.save()
        
    def delete_tags(self):
        self.delete()

class Location(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()

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

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()
        
    @classmethod
    def search_image(cls,search_term):
        images=cls.objects.filter(name__icontains=search_term)
        return images
    
        
    @classmethod
    def update_image(cls,id):
        images=cls.objects.filter(id=id).update(id=id)
        return images
    
    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(pk=id)
        return images
    
    @classmethod
    def filter_by_tag(cls,tags):
        images=cls.objects.filter(tags=tags)
        return images
    
    @classmethod
    def filter_by_location(cls,location):
        images=cls.objects.filter(location=location)
        return images
    
    @classmethod
    def delete_image_by_id(cls,id):
        images=cls.object.filter(pk=id)
        images.delete()
        
    

class Profile(models.Model):
    bio=models.TextField(max_length=100,null=True,blank=True,default="bio")
    profilepic=models.ImageField(upload_to='picture/',null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,related_name="profile")
    following=models.ManyToManyField(User,related_name="following",blank=True)
    followers=models.ManyToManyField(User,related_name="followers",blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def follow_user(self,follower):
        return self.following.add(follower)

    def is_following(self,check_user):
        return check_user in self.following.all()

    def get_number_of_following(self):
            if self.following.count():
                return self.following.count()
            else:
                return 0

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def unfollow_user(self,to_unfollow):
        return self.following.remove(to_unfollow)

    @classmethod
    def search_users(cls,search_term):
        profiles=cls.objects.filter(user__username__icontains=search_term)
        return profiles
    
    
    