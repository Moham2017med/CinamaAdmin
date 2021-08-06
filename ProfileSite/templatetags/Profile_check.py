from django import template
from ProfileSite.models import Profile
from django.shortcuts import render

register=template.Library()


@register.filter(name='has_profile')
def has_Profile(user):
    try:
           profile =Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return False
    return True
def NavigatioMenu(request):
    userNav=request.user
    MyProfile = Profile.objects.get(slug=request.user)
    context = {
        "MyPro": MyProfile,
        "userNav":userNav

    }
    return render(request, "AdminProfile/Sections/NavigatioMenu.html", context)





