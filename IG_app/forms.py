from django import forms
from .models import Comments, Profiles, Images

class NewImageForm(forms.ModelForm):
    image = forms.ImageField()
    caption = forms.CharField(max_length=100)
    class Meta: 
        model = Images
        exclude = ['posted','profile']
    
class PostComment(forms.ModelForm):
    class Meta: 
        model = Comments
        exclude = ['image','posted','user']

class NewProfile(forms.ModelForm):
    class Meta:
        models = Profiles
        exclude = ['user',]

