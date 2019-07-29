from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostComment,NewImageForm,NewProfile
from .models import Images, Profiles, Comments 

# Create your views here.
def index(request):
    images = Images.get_all_images()
    return render(request,'index.html',{'images':images})

@login_required(login_url='/accounts/login/')
def profile(request,username):
    user = User.objects.get(username=username)
    profile = Profiles.filter_profile_by_id(user.id)
    title = f'{user.username}\'s Profile '
    images = Images.get_profile_images(user.id)
    return render(request, 'profile/profile.html',{'title':title,'users':user,'profile':profile,'images':images})
    
@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('editProfile')
    else:
        form = NewProfile()
            
    return render(request,'profile/edit_profile.html',{'form':form})
    
@login_required(login_url='/accounts/login/')
def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
            return redirect('profile',username=request.user)
    else:
        form = NewImageForm()
    return render(request,'profile/new_image.html',{'form':form})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profiles.get_profile_by_name(search_term)
        message = f'{search_term}'
        
        return render(request,'search.html',{'message':message,'profiles':profiles})
    else:
        message = 'Search Username'
        return render(request,'search.html',{'message':message})
    
@login_required(login_url='/accounts/login/')
def view_single_image(request,image_id):
    image = Images.get_image_by_id(image_id)
    comments = Comments.get_comment_by_image(image_id)
    current_user = request.user
    if request.method == 'POST':
        form = PostComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect('singleImage',image_id=image_id)
    else:
        form = PostComment()
    return render(request, 'image.html',{'image':image,'form':form,'comments':comments})
