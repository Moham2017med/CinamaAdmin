from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from .models import *
from VideoApp.models import *
from Posts.models import *



def JudgementComitysView(request,id):

    MyProfile = Profile.objects.get(slug=request.user)
    Judgementy = JudgementComitys.objects.filter(MovieSections=id)
    movieSection = MovieSection.objects.all()
    channel_videos = VideoFiles.objects.filter(MovieSections=id)
    # request.POST['JudgementComity']

    context = {
        "MyPro": MyProfile,
        "Judgementy": Judgementy,
        'movieSection': movieSection,
        'my_videos':channel_videos


    }

    return render(request, "AdminProfile/Competitions/JudgementComitys/JudgementHome.html", context)

def JudgementComitysUserView(request,slug):
    MyProfile = Profile.objects.get(slug=slug)

    movieSection = MovieSection.objects.all()
    channel_videos = VideoFiles.objects.filter(channel=MyProfile)

    # request.POST['JudgementComity']
    movie = MovieSection.objects.all()

    context = {
        "MyPro": MyProfile,
        'movieSection': movieSection,
        'my_videos': channel_videos,
        'movie': movie,

    }

    return render(request, "Web/UserProFile/MovieSection.html", context)


def JudgementComitysUserVideos(request, video_id):
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

    return render(request, "Web/UserProFile/JudgementComity_1.html", context)


def JudgementComitysViewWeb(request,id):

    MyProfile = Profile.objects.get(slug=request.user)
    Judgementy = JudgementComitys.objects.filter(MovieSections=id)
    movieSection = MovieSection.objects.all()
    channel_videos = VideoFiles.objects.filter(MovieSections=id)
    # request.POST['JudgementComity']
    movie = MovieSection.objects.get(id=id)

    context = {
        "MyPro": MyProfile,
        "Judgementy": Judgementy,
        'movieSection': movieSection,
        'my_videos':channel_videos,
        'movie':movie,


    }

    return render(request, "Web/CompetitionWeb/MovieSection.html", context)

def JudgementComitysViewWebHome(request,id_M):

    MyProfile = Profile.objects.get(slug=request.user)
    Judgementy = JudgementComitys.objects.get(id=id_M)
    movieSection = MovieSection.objects.all()
    channel_videos = VideoFiles.objects.filter(MovieSections=Judgementy.MovieSections,Stages=Judgementy.Stages)
    # request.POST['JudgementComity']
    movie = MovieSection.objects.get(id=Judgementy.MovieSections.id)

    context = {
        "MyPro": MyProfile,
        "Judgementy": Judgementy,
        'movieSection': movieSection,
        'my_videos':channel_videos,
        'movie':movie,


    }

    return render(request, "Web/CompetitionWeb/JudgementComity_Home.html", context)


def JudgementComitysPartView(request,video_id):
    video = get_object_or_404(VideoFiles, id=video_id)
    MyProfile = Profile.objects.get(slug=request.user)
    Comitys=Profile.objects.filter(SpecialtyType=2)

    Judgementy = JudgementComitys.objects.filter(video=video_id,Stages=video.Stages,MovieSections=video.MovieSections)
    context = {
        "MyPro":MyProfile,
        "Comitys": Comitys,
        "my_videos": video,
        "Judgementy":Judgementy,


    }
    return render(request, "AdminProfile/Competitions/Participants/JudgementComitys.html", context)


def AddComitys(request,slug,video_id):
    user = request.user
    video = get_object_or_404(VideoFiles, id=video_id)
    MyProfile = get_object_or_404(Profile, slug=slug)
    MyPro = Profile.objects.get(user=user)


    if request.method == "POST" :
        form = JudgementComitysForm(request.POST, request.FILES)
        if form.is_valid():



            description = form.cleaned_data.get('description')

            JudgementComitys.objects.create(title=MyProfile.FullName , user=request.user,JudgementComity=MyProfile,
                                Stages=video.Stages,MovieSections=video.MovieSections, description=description,video=video)

            return redirect('JudgementComitysPartView',video.id)



    form = JudgementComitysForm()
    context = {
        'MyPro':MyPro,
        "form": form,
        "Pro":MyProfile,
        "my_videos": video,
    }
    return render(request,"AdminProfile/Competitions/Participants/AddComitys.html", context)


def ParticipantsView(request,id):
    MyProfile = Profile.objects.get(slug=request.user)
    profile = Profile.objects.all()

    Stages_videos = MovieSection.objects.all()
    channel_videos = VideoFiles.objects.filter(MovieSections=id)


    context = {
        "MyPro": MyProfile,
        "my_videos": channel_videos,
        "profile": profile,
        'Stag':Stages_videos



    }
    return render(request, "AdminProfile/Competitions/Participants/Participants.html", context)

def MyParticipants(request):
    MyProfile = Profile.objects.get(slug=request.user)
    profile = Profile.objects.all()
    posts = Post.objects.filter(author=request.user).order_by('-created_date')
    channel_videos = VideoFiles.objects.filter(channel=MyProfile)
    context = {
        "MyPro": MyProfile,
        "my_videos": channel_videos,
        "posts": posts,
        "profile": profile,


      }
    return render(request, "AdminProfile/Participants/Participants.html", context)

def JudgementyMyParticipantsView(request,video_id):
    video = get_object_or_404(VideoFiles, id=video_id)
    MyProfile = Profile.objects.get(slug=request.user)
    Judgementy = JudgementComitys.objects.all()
    Stages_videos = MovieSection.objects.all()
    #request.POST['JudgementComity']




    context = {
        "MyPro": MyProfile,
        "my_videos": video,
        "Judgementy" : Judgementy,
        'Stag': Stages_videos,

      }
    return render(request, "AdminProfile/Competitions/Participants/JudgementyMyParticipantsView.html", context)




