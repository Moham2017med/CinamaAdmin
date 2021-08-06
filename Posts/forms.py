from django import forms
from django.contrib.auth.models import User
from . models import  Post, Comment
from ProfileSite.models import Profile

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
        widgets = {

            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(
                attrs={'class': 'form-control'}),

        }
class videoCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['video', 'caption','imageVideo']
        widgets = {
            'imageVideo': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(
                attrs={'class': 'form-control'}),

        }
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class videoform(forms.ModelForm):
    class Mete:
        model = Post
        fields = ('video', 'caption','imageVideo')