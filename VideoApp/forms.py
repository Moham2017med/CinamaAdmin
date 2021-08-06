from django import forms
from .models import VideoFiles,VideoComment


class VideoFilesFormAll(forms.ModelForm):
    class Meta:
        model=VideoFiles
        fields=('__all__')

class videoForm(forms.ModelForm):



    class Meta:
        model = VideoFiles
        fields = ['title', 'video','description','visibility','thumbnail']
        widgets = {

            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'visibility': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }

class videoUpdateForm(forms.ModelForm):
    class Meta:
        model = VideoFiles
        fields = ['title', 'video', 'description', 'visibility', 'thumbnail']
        widgets = {

            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'visibility': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class AddVideo_ParticipantsForm(forms.ModelForm):



    class Meta:
        model = VideoFiles
        fields = ['title', 'video','description','visibility','thumbnail','Stages','MovieSections']
        widgets = {

            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'Stages': forms.Select(attrs={'class': 'form-control'}),
            'MovieSections': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'visibility': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),

        }
"""
class AddParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ['title', 'video','Participanted','JudgementComity']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.Select(attrs={'class': 'form-control'}),
            'JudgementComity': forms.Select(attrs={'class': 'form-control'}),
            'Participanted': forms.Select(attrs={'class': 'form-control'}),


        }
"""