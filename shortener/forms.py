from urllib.parse import urlparse
from django import forms
from shortener.utils import url_count_changer
from django.contrib.auth.forms import UserCreationForm
from shortener.models import Users, ShortenedUrls
from django.utils.translation import gettext_lazy as _

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
    
class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrls
        fields = ["nick_name", "target_url"]
        labels = {
            "nick_name": _("별칭"),
            "target_url": _("URL"),
        }
        widgets = {
            "nick_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL을 구분하기 위한 별칭"}),
            "target_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "포워딩될 URL"}),
        }

    def save(self, request, commit=True):
        instance = super(UrlCreateForm, self).save(commit=False)
        instance.creator_id = request.user.id
        instance.target_url = instance.target_url.strip()
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
            else:
                url_count_changer(request, True)
        return instance

    def update_form(self, request, url_id):
        instance = super(UrlCreateForm, self).save(commit=False)
        instance.target_url = instance.target_url.strip()
        ShortenedUrls.objects.filter(pk=url_id, creator_id=request.user.id).update(
            target_url=instance.target_url, nick_name=instance.nick_name
        )
            