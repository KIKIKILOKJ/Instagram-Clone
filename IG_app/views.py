from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import NewsLetterForm,NewImageForm,UpdateBioForm
from .models import Image,Location,tags,NewsLetterRecipients,Profile

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

#Function to allow searching of users by their username
def search_users(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_users(search_term)
        return render(request, 'search.html', {"profiles":searched_users,"user":search_term})
    else:
        message="You have not searched for anyone"
        return render(request, 'search.html', {"message":message})

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

def personal_profile_page(request,username=None):
    if not username:
        username = request.user.username
        images=Image.objects.filter(user_id=username)
        return render (request, 'user.html', {'images':images, 'username': username})
