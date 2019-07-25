from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import NewsLetterForm
from .models import Image,Location,tags,NewsLetterRecipients

# Function to display all Images
tags = tags.objects.all()
def index(request):
    images=Image.objects.all()
    location=Location.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('index')
    else:
        form = NewsLetterForm()
    return render(request, 'index', {"location":location,"tags":tags,"images":images,"letterForm":form})