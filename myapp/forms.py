from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from myapp.models import Post
from django.forms import widgets

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter Password'}))
 password1 = forms.CharField(label='Password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter Password'}))
 class Meta:
  model = User 
  fields = ['username','first_name','last_name','email']
  labels = {'email':'Email', 'first_name':'First name','last_name':'Last name'}
  widgets = {
    'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
    'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),
    'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),
    'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email','required':'true'}),
  }

class LoginForm(AuthenticationForm):
 username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username','autofocus':True}))
 password = forms.CharField(label='Password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter Password'}))
 class Meta:
  model = User

class ChangepasswordForm(PasswordChangeForm):
 old_password = forms.CharField(label='Old password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter old password'}))
 new_password1 = forms.CharField(label='New password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter new password'}))
 new_password2 = forms.CharField(label='Confirm new password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter new password again'}))
 def __init__(self, *args, **kwargs):
    request = kwargs.pop("request")
    super(ChangepasswordForm, self).__init__(request.user, *args, **kwargs)
 class Meta:
  model = User
  
class ChangepasswordForm1(SetPasswordForm):
 new_password1 = forms.CharField(label='New password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter new password'}))
 new_password2 = forms.CharField(label='Confirm new password',widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter new password again'}))
 def __init__(self, *args, **kwargs):
    request = kwargs.pop("request")
    super(ChangepasswordForm1, self).__init__(request.user, *args, **kwargs)
 class Meta:
  model = User  
  
class EditUserProfileForm(UserChangeForm):
 password = None
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'first_name':'First name','last_name':'Last name','email':'Email'}
  
class EditAdminProfileForm(UserChangeForm):
 password = None
 class Meta:
  model = User
  fields = '__all__'
  labels = {'first_name':'First name','last_name':'Last name','email':'Email','date_joined':'Joined date','last_login':'last login'}
  
  
class ImageForm(forms.ModelForm):
 class Meta:
  model = Post
  fields = ['photo']
  labels = {'photo':''}
