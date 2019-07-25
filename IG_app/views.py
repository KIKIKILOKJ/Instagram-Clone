from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import NewsLetterForm,NewImageForm,UpdateBioForm
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

def new_image(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateBioForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = UpdateBioForm()
    return render(request, 'edit_profile.html', {"form": form})