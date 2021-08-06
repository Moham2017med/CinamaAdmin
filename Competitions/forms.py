from django import forms
from .models import JudgementComitys
from ProfileSite.models import Profile


class JudgementComitysForm(forms.ModelForm):


    class Meta:
        model = JudgementComitys
        fields = [ 'description']
        widgets = {

            'description': forms.Textarea(attrs={'class': 'form-control'}),



        }

class JudgementComitysAddVideoForm(forms.ModelForm):


    class Meta:
        model = JudgementComitys
        fields = ['video']



class JudgementComitysFormAll(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('__all__')





