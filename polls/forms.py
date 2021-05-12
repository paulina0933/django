from django import forms
from .models import Post

class Post_Form(forms.Form):
    title = forms.CharField()
    contents = forms.CharField()

    image = forms.ImageField()

class Create_User_Form(forms.Form):
    nick = forms.CharField()
    about = forms.CharField()
    login = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


    # WTF serchform check it
