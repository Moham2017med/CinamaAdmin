from django import forms
from . models import  *
from ckeditor.fields import RichTextField


class ArticlesCreateForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','image', 'caption']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),




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
