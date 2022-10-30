from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser

class RegisterForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Confirm',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')
        fields=['email','username']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    class Meta:
        model=get_user_model()
        fields=['username','password']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'password':forms.PasswordInput(attrs={'class':'form-control'})}
