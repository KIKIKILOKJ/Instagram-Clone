from django import forms
from .models import Image
class NewsLetterForm(forms.Form):
    your_name =forms.CharField(label='First Name')
    email = forms.EmailField(label='Email')

class NewImageForm(forms.Modelform):
    class meta:
        model=Image
        exclude=['user','likes']