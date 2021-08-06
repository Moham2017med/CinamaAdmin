from django import forms
from .models import *

class YouTubeFormAll(forms.ModelForm):
    class Meta:
        model=YouTube
        fields=('__all__')


class LecturesFormAll(forms.ModelForm):
    class Meta:
        model=Lectures
        fields=('__all__')


class YouTubeForm(forms.ModelForm):


    class Meta:
        model = YouTube
        fields = ['title', 'YouTubeType','linke','image','content']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'YouTubeType': forms.Select(attrs={'class': 'form-control'}),
            'linke': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),

        }






class YouTubeModelForm(forms.ModelForm):

    content = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':2 ,'class': 'input-value text-right'
                                                                    ,'placeholder': 'كتابة المنشور هنا'}))


    class Meta:
        model = YouTube
        fields = ( 'title','YouTubeType','linke', 'content','image')
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'كتابة عنوان المنشور هنا', 'class': 'input-value text-right'}),

        }

