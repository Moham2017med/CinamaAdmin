from django import forms
from .models import SpecialtyType,Specialty,Profile


class ProfileWebForm(forms.ModelForm):

    SpecialtyType = forms.ModelChoiceField(queryset=SpecialtyType.objects.all(), label="")
    Specialty = forms.ModelChoiceField(queryset=Specialty.objects.all(), label="")



    class Meta:
        model = Profile
        fields = ['FullName','Phone','State','gender','age',  'Profile_Icon','description']
        widgets={

            'FullName': forms.TextInput(attrs={'placeholder': 'enter your channel name', 'class': 'input-value'}),
            'Phone': forms.TextInput(attrs={'placeholder': 'enter your channel name', 'class': 'input-value'}),
            'State': forms.Select(attrs={'placeholder': 'enter your channel name','style':'color: wheat;background: black'}),
            'age': forms.Select(attrs={'placeholder': 'enter your channel name','style':'color: wheat;background: black'}),
            'gender': forms.Select(attrs={'placeholder': 'enter your channel name','style':'color: wheat;background: black'}),
            'Profile_Icon': forms.FileInput(attrs={'placeholder': 'enter your channel name'}),
            'description': forms.Textarea(attrs={'placeholder': 'enter your channel name','style':'color: wheat;background: black'}),

        }

class ProfileWebEditForm(forms.ModelForm):

    SpecialtyType = forms.ModelChoiceField(queryset=SpecialtyType.objects.all(), label="")
    Specialty = forms.ModelChoiceField(queryset=Specialty.objects.all(), label="")



    class Meta:
        model = Profile
        fields = ['FullName','Phone','State','gender','age',  'Profile_Icon','description','address',
                  'emaiAddress','Zoom','Skype','YouTube','Instagram','Snapchat','Twitter','Facebook']

        widgets={
            'State': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'YouTube': forms.TextInput(attrs={'class': 'form-control'}),
            'Instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'Snapchat': forms.TextInput(attrs={'class': 'form-control'}),
            'Twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'Facebook': forms.TextInput(attrs={'class': 'form-control'}),

        }







