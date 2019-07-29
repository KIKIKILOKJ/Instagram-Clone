from django import forms
from .models import Image,Profile,Review
class NewsLetterForm(forms.Form):
    your_name =forms.CharField(label='First Name')
    email = forms.EmailField(label='Email')

class NewImageForm(forms.Form):
    class meta:
        model=Image
        exclude=['user','likes']
        
class UpdateBioForm(forms.Form):
    class meta:
        model=Profile
        exclude=['user','followers','following']
        
class ReviewForm(forms.ModelForm):
    class Meta:

        model = Review
        fields = ('comment',)