from django.test import TestCase
from .models import Images, Profiles, Comments
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.user= User(username='',email='', password='')
        self.user.save()

        self.profile=Profiles(images='',bio='',user=self.user)
        self.profile.save()
        
        self.image = Images(image='',caption='',pub_date='',profile=self.user())
        self.image.save_image()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Images))

    def test_save_image(self):
        self.image.save_image()
        images= Images.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_caption(self):
        self.image.save_image()
        Image.update_caption(self.image.id)
        self.assertEqual("",self.image.caption)


    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Images.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_id(self):
        image_id = id
        self.image.objects.get(pk=id)
        self.assertTrue(pk=id)

    def tearDown(self):
        Images.objects.all().delete()

class ProfileTestClass(TestCase):
    def setup (self):
        self.user= User(username='',email='', password='')
        self.user.save()

        self.profile=Profiles(images='',bio='',user=self.user)
        self.profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profiles))

    def test_save_method(self):
        self.bio.save_bio()
        profile =Profiles.objects.all()
        self.assertTrue(len(profile) > 0)


    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profiles.objects.all()
        self.assertTrue(len(profile) == 0)

    def tearDown(self):
        Image.objects.all().delete()

class CommentsTestClass(TestCase):


    def setup (self):
        self.user= User(username='',email='', password='')
        self.user.save()

        self.profile=Profiles(images='',bio='',user=self.user)
        self.profile.save()

        self.comment=Comments(comment='',image=self.image, user=self.profile())

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        self.comment.save_comment()
        comments =Comments.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comments(self):
        self.comments.save_comments()
        self.comments.delete_comments()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) == 0)

    def tearDown(self):
        Comments.objects.all().delete()
