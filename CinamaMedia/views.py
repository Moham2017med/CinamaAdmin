from django.shortcuts import render, redirect
from ProfileSite.models import Profile
from .forms import YouTubeForm
from .models import YouTube,Lectures
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def DashboardCinamaMedia(request):
    userNav=request.user
    MyProfile = Profile.objects.get(slug=request.user)

    context = {
        "MyPro": MyProfile,
        "userNav":userNav

    }
    return render(request, "AdminProfile/CinamaMedia/index.html", context)

def LecturesViwe(request):
    userNav=request.user
    lectures = Lectures.objects.all()

    context = {
        "lecing": lectures,
        "userNav":userNav

    }
    return render(request, "Web/WebProfile/LecturesWeb.html", context)
def LecturesUserViwe(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    userNav=request.user
    lectures = Lectures.objects.all()

    context = {
        "lecing": lectures,
        "userNav":userNav,
        "MyPro": MyProfile,

    }
    return render(request, "Web/UserProFile/LecturesWeb.html", context)

def YouTubeProfile(request):
    MyProfile = Profile.objects.get(slug=request.user)
    youTube = YouTube.objects.filter(author=MyProfile)
    context = {
        "MyPro": MyProfile,
        'youTube': youTube,
    }
    return render(request, "AdminProfile/CinamaMedia/YouTubeProfile.html", context)

def AddYouTube(request):
    user = request.user
    Profi = Profile.objects.get(user=user)

    if request.method == "POST":
        form = YouTubeForm(request.POST, request.FILES)
        if form.is_valid():

            title = form.cleaned_data.get('title')
            YouTubeType = form.cleaned_data.get('YouTubeType')
            linke = form.cleaned_data.get('linke')
            image = form.cleaned_data.get('image')
            content = form.cleaned_data.get('content')

            YouTube.objects.create(title=title, author=Profi,
                                YouTubeType=YouTubeType,linke=linke, image=image, content=content)

        return redirect('YouTubeProfile')

    form = YouTubeForm()
    context = {
        "form": form,
    }
    return render(request, "AdminProfile/CinamaMedia/AddYouTube.html", context)

def AddYouTubeWeb(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    user = request.user
    Profi = Profile.objects.get(user=user)

    if request.method == "POST":
        form = YouTubeForm(request.POST, request.FILES)
        if form.is_valid():

            title = form.cleaned_data.get('title')
            YouTubeType = form.cleaned_data.get('YouTubeType')
            linke = form.cleaned_data.get('linke')
            image = form.cleaned_data.get('image')
            content = form.cleaned_data.get('content')

            YouTube.objects.create(title=title, author=Profi,
                                YouTubeType=YouTubeType,linke=linke, image=image, content=content)

        return redirect('ChannelMyVideosUserWeb', MyProfile.slug)

    form = YouTubeForm()
    context = {
        "form": form,
        'MyPro':MyProfile
    }
    return render(request, "Web/UserProFile/info/AddYuTube.html", context)



def YouTubeDelete(request, id):
    youTube=YouTube.objects.get(id=id)
    if request.method=="POST":
        youTube.delete()
        return redirect("YouTubeProfile")
    context={
        "youTube":youTube
    }
    return render(request, "AdminProfile/CinamaMedia/YouTube_delete.html", context)

class YouTubeUpdateView(LoginRequiredMixin, UpdateView):
    form_class = YouTubeForm
    model = YouTube
    template_name = 'AdminProfile/CinamaMedia/YouTube_Update.html'
    success_url = reverse_lazy('YouTubeProfile')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be the author of the post in order to update it")
            return super().form_invalid(form)


