
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileWebForm,ProfileWebEditForm
from .models import *
from googletrans import Translator
from Posts.models import Post
from Articles.models import Articles
from CinamaMedia.models import YouTube,YouTubeTypes,CinamaMedias
from VideoApp.models import VideoFiles, ViewCount,MovieSection,Stages
from Competitions.models import JudgementComitys

def CompetitionsWeb(request):
    movieSection = MovieSection.objects.all()
    stages = Stages.objects.all()
    context = {

        'movieSection': movieSection,
        'stages': stages,


    }
    return render(request, "Web/Sections/Competitions.html",context)
def WhoAreWeWeb(request):

    return render(request, "Web/Sections/WhoAreWe.html")
def indexPostsWeb(request,id):
    MyPros = get_object_or_404(Profile, id=id)
    MyProfile = Profile.objects.all()
    articles = Articles.objects.all().order_by('-updatedArticles')
    post = Post.objects.all().order_by('-created_date')
    youTube = YouTube.objects.all().order_by('-created')
    youTubeTypes = YouTubeTypes.objects.all()
    video = VideoFiles.objects.all().order_by('-uploaded')
    movieSection = MovieSection.objects.all()
    stages = Stages.objects.all()
    Judgementy = Stages.objects.all()

    context = {
        'MyPros':MyPros,
        'MyPro':MyProfile,
        'post': post,
        'youTubeTypes': youTubeTypes,
        'youTube':youTube,
        'articles':articles,
        'video':video,
        'movieSection':movieSection,
        'stages':stages,
        'Judgementy':Judgementy,


    }
    return render(request, "Web/postsWeb/index.html", context)

def indexHome(request):

    MyProfile = Profile.objects.all()
    articles = Articles.objects.all().order_by('-created_date')
    post = Post.objects.all().order_by('-created_date')
    youTube = YouTube.objects.all().order_by('-created')
    youTubeTypes = YouTubeTypes.objects.all()
    video = VideoFiles.objects.all().order_by('-uploaded')
    movieSection = MovieSection.objects.all()
    stages = Stages.objects.all()
    Judgementy = Stages.objects.all()
    cinama = CinamaMedias.objects.get(id=1)

    context = {
        'MyPro':MyProfile,
        'post': post,
        'youTubeTypes': youTubeTypes,
        'youTube':youTube,
        'articles':articles,
        'video':video,
        'movieSection':movieSection,
        'stages':stages,
        'Judgementy':Judgementy,
        'cin': cinama,


    }
    return render(request, "Web/index.html", context)
def indexHomeUser(request,slug):
    user=request.user.id
    MyProfile = Profile.objects.get(slug=slug)
    MyPros = Profile.objects.all()
    articles = Articles.objects.filter(profile=MyProfile).order_by('-created_date')
    articlesVip = Articles.objects.all().order_by('-created_date')
    post = Post.objects.filter(profile=MyProfile).order_by('-created_date')
    youTube = YouTube.objects.filter(author=MyProfile).order_by('-created')
    youTubeTypes = YouTubeTypes.objects.all()
    video = VideoFiles.objects.filter(channel=MyProfile).order_by('-uploaded')
    videoVip = VideoFiles.objects.filter().order_by('-uploaded')
    movieSection = MovieSection.objects.all()
    stages = Stages.objects.all()
    Judgementy = Stages.objects.all()
    cinama = CinamaMedias.objects.get(id=1)

    context = {
        'MyPro':MyProfile,
        'post': post,
        'youTubeTypes': youTubeTypes,
        'youTube':youTube,
        'articles':articles,
        'video':video,
        'movieSection':movieSection,
        'stages':stages,
        'Judgementy':Judgementy,
        'cin': cinama,
        'MyPros':MyPros,
        'articlesVip':articlesVip,
        'videoVip': videoVip,


    }
    return render(request, "Web/UserProFile/index.html", context)

def VideoDetails(request, video_id):
    video = get_object_or_404(VideoFiles, id=video_id)
    vid_cat = video.channel.Specialty.Specialty
    suggested_videos = VideoFiles.objects.filter(channel__Specialty__Specialty=vid_cat).exclude(video=video.video)



    ip = request.META['REMOTE_ADDR']

    if not ViewCount.objects.filter(video=video, session=request.session.session_key):
        view = ViewCount(video=video, ip_address=ip, session=request.session.session_key)
        view.save()
    video_views = ViewCount.objects.filter(video=video).count()

    context = {
        "my_video": video,
        "view_count": video_views,
        "recommended_videos": suggested_videos,


    }

    return render(request, 'AdminProfile/MyVideo/Video_details.html', context)
def DashboardPro(request):
    userNav=request.user
    MyProfile = Profile.objects.get(slug=request.user)
    context = {
        "MyPro": MyProfile,
        "userNav":userNav

    }
    return render(request, "AdminProfile/MyProfile/index.html", context)
def ProfileViwe(request):
    
    MyProfile = Profile.objects.get(slug=request.user)
    context = {
        "MyPro": MyProfile,
      }
    return render(request, "AdminProfile/index.html", context)





def MyProfile(request, slug):
    MyProfile = Profile.objects.get(slug=slug)
    profile = Profile.objects.all()
    Followers = Profile.objects.filter(subcribers__id=request.user.id).count()
    Following = Profile.objects.filter(subcribers__id=MyProfile.id).count()
    friending = Profile.objects.filter(subcribers__id=MyProfile.id)
    posts = Post.objects.filter(author=request.user).order_by('-created_date')
    translator = Translator()




    if request.method == "POST":
        form = ProfileWebEditForm(request.POST, request.FILES, instance=MyProfile)
        if form.is_valid():
            form.save()
            return redirect("/", slug=request.user.username)
    else:
        form = ProfileWebEditForm(instance=MyProfile)


    context = {
        "MyPro": MyProfile,
        "edit_form": form,
        "Followers": Followers,
        "Following": Following,
        "posts": posts,
        "profile": profile,
        "friending": friending



      }
    return render(request, "AdminProfile/MyProfile/MyProfile.html", context)




def WebProfileWeb_info(request):


    TSpecialty = SpecialtyType.objects.all()
    MSpecialty = Specialty.objects.all()


    u = Profile()
    user=request.user
    emaiAddress=request.user.email
    us = Profile.objects.filter(user=user).count()

    if request.method =="POST":
        form=ProfileWebForm(request.POST, request.FILES)
        if us == 0:
            if form.is_valid():


                FullName = form.cleaned_data.get('FullName')
                Phone = form.cleaned_data.get('Phone')
                Profile_Icon=form.cleaned_data.get('Profile_Icon')
                u.SpecialtyType = form.cleaned_data['SpecialtyType']
                u.Specialty = form.cleaned_data['Specialty']
                u.State = form.cleaned_data['State']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                description = form.cleaned_data.get('description')


                Profile.objects.create(FullName=FullName, user=user,slug=user.username,
                                       Phone=Phone,SpecialtyType=u.SpecialtyType,Specialty=u.Specialty,
                                       Profile_Icon=Profile_Icon,State=u.State,age=age,gender=gender,
                                       description=description,emaiAddress=emaiAddress)
                return redirect("home")
        else:
            form.add_error(None, "You need to be the author of the post in order to update it")

            return redirect("home")

        return render(request, "Web/WebProfile/WebProfileWeb_info.html")

    else:
        form=ProfileWebForm()
        context={
            "form":form,
            "TS": TSpecialty,
            "MS": MSpecialty,

        }
        return render(request, "Web/WebProfile/WebProfileWeb_info.html", context)


def find_friends(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    profile = Profile.objects.all()

    context = {
        "profile": profile,
        "MyPro":MyProfile
    }
    return render(request, "AdminProfile/MyProfile/find_friends.html", context)
def friends(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    profile = Profile.objects.all()
    Followers = Profile.objects.filter(subcribers__id=request.user.id).count()
    Following = Profile.objects.filter(subcribers__id=MyProfile.id).count()
    friending = Profile.objects.filter(subcribers__id=MyProfile.id)
    posts = Post.objects.filter(author=request.user).order_by('-created_date')

    context = {
       "Followers":Followers,
       "Following": Following,
        "posts":posts,
        "profile": profile,
        "MyPro":MyProfile,
        "friending":friending
    }
    return render(request, "AdminProfile/MyProfile/frienud.html", context)












