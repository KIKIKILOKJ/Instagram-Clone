from django import forms
from .models import Image,Profile
class NewsLetterForm(forms.Form):
    your_name =forms.CharField(label='First Name')
    email = forms.EmailField(label='Email')

class NewImageForm(forms.Modelform):
    class meta:
        model=Image
        exclude=['user','likes']
        
class UpdateBioForm(forms.ModelForm):
    class meta:
        model=Profile
        exclude=['user','followers','following']