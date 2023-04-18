from django import forms
from django.contrib.auth.forms import UserCreationForm
from shortener.models import Users

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text='Optional', label='이름')
    username = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, required=True)
    
    class Meta:
        model=Users
        fields=(
            'full_name',
            'username',
            'email',
            'password1',
            'password2'
        )

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=254, 
        required=True, 
        widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"email"})
        )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"password"})
        )
    remember_me = forms.BooleanField(
        required=False,
        disabled=False,
        widget=forms.CheckboxInput(attrs={"class":"custom-control-input","id":"_loginRememberMe"})
        )
    