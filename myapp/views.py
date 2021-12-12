from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect,get_object_or_404,redirect
from myapp.forms import ChangepasswordForm1,SignUpForm, LoginForm, ChangepasswordForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from myapp.forms import ImageForm
from myapp.models import Post
from django.urls import reverse
#Home
def home(request):
 return HttpResponseRedirect('/login/')

#signup view
def sign_up(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():
   fm.save()
   fm = SignUpForm()
   messages.add_message(request, messages.SUCCESS, 'Registered successfully')
 else:    
  fm = SignUpForm()
 return render(request, 'myapp/signup.html', {'form':fm})


#login view
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
    fm = LoginForm(request=request, data=request.POST)
    if fm.is_valid():
      uname = fm.cleaned_data['username']
      upass = fm.cleaned_data['password']
      user = authenticate(username=uname, password=upass)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect('/profile/')
  else:
    fm = LoginForm()
  return render(request, 'myapp/login.html', {'form':fm})
 else:
  return HttpResponseRedirect('/profile/')

@login_required
#Profile
def user_profile(request):
 if request.method == 'POST':
  fm = EditUserProfileForm(request.POST, instance=request.user)
  if fm.is_valid():
   fm.save()
   messages.success(request, 'Profile updated successfully')
 else:
  fm = EditUserProfileForm(instance=request.user)
  img = Post.objects.filter(user=request.user)
  return render(request, 'myapp/home.html', {'fname':request.user.first_name,'lname':request.user.last_name,'form':fm,'img':img})


#dashboard
def dashboard(request):
 if request.user.is_authenticated:
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
     user = request.user
     photo = form.cleaned_data.get("photo")
     obj = Post.objects.create(user=user,photo=photo)
     obj.save()
     return HttpResponseRedirect('/dashboard')
  else:
    form = ImageForm()
    img = Post.objects.all()
    return render(request,'myapp/dashboard.html',{'form':form,'img':img})
 else:
  return HttpResponseRedirect('/login/')


#Logout
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')

#changepassword with old password
def user_change_pass(request):
 if request.user.is_authenticated: 
  if request.method == 'POST':
    fm = ChangepasswordForm(request=request, data=request.POST)
    if fm.is_valid():
     fm.save()
     update_session_auth_hash(request, fm.user)
     messages.add_message(request,messages.SUCCESS,'Password changed successfully')
     return HttpResponseRedirect('/profile/')
  else:
    fm = ChangepasswordForm(request=request)
  return render(request, 'myapp/changepass.html', {'form':fm})
 else:
   return HttpResponseRedirect('/profile/') 
 
 #changepassword without old password
def user_change_pass1(request):
 if request.user.is_authenticated: 
  if request.method == 'POST':
    fm = ChangepasswordForm1(request=request, data=request.POST)
    if fm.is_valid():
     fm.save()
     update_session_auth_hash(request, fm.user)
     messages.add_message(request,messages.SUCCESS,'Password changed successfully')
     return HttpResponseRedirect('/profile/')
  else:
    fm = ChangepasswordForm1(request=request)
  return render(request, 'myapp/changepass1.html', {'form':fm})
 else:
   return HttpResponseRedirect('/profile/') 
 
@login_required
def liked_video(request,id):
 user = request.user
 if request.method == 'POST':
  video_id = request.POST['video_id']
  get_video = get_object_or_404(Post,id=video_id)
  if user in get_video.likes.all():
   get_video.likes.remove(user)
   btnlike = 'far fa-heart'
   Like = False
  else:
   get_video.likes.add(user)
   btnlike = 'fas fa-heart'
   Like = True
    
  data = {
    'like':Like,
    'btnlike':btnlike,
    'likes_count':get_video.likes.all().count()
  }
  return JsonResponse(data)
 return redirect('/dashboard')




  
  
 
 
