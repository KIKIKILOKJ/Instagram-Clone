from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import NewsLetterForm,NewImageForm,UpdateBioForm,ReviewForm
from .models import Image,Location,tags,NewsLetterRecipients,Profile,Review
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Function to display all Images
tags = tags.objects.all()
@login_required(login_url='/accounts/login/')
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
            HttpResponseRedirect('index.html')
    else:
        form = NewsLetterForm()
    return render(request, 'index.html', {"location":location,"tags":tags,"images":images,"letterForm":form})

#Function to allow searching of users by their username
def search_users(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_users(search_term)
        return render(request, 'search.html', {"profiles":searched_users,"user":search_term})
    else:
        message="You have not searched for anyone"
        return render(request, 'search.html', {"message":message})
    
def search_image(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        return render(request, 'search.html', {"pictures": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html', {"message": message})

def image(request, id):
    image = Image.objects.get(pk = id)
    current_user = request.user
    comments = Review.get_comment(Review, id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            review = Review()
            review.image = image
            review.user = current_user
            review.comment = comment
            review.save()
        else:
            form = ReviewForm()

    return render(request, 'image.html', {"image": image,'form':ReviewForm,'comments':comments,})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index.html')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def person_profile_page(request,username=None):
    if not username:
        username = request.user.username
        images=Image.objects.filter(user_id=username)
        profile=Profile.objects.get(user=user)
        return render (request, 'user.html', {'images':images, 'username': username,"profile":profile})

@login_required(login_url='/accounts/login/')
def my_profile(request,username=None):
    if not username:
        username = request.user.username
        images = Image.objects.filter(user_id=username)

        return render(request, 'profile.html')
                #locals())
