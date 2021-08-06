from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView

from .forms import videoForm,videoUpdateForm,AddVideo_ParticipantsForm
from .models import Channel, VideoFiles, ViewCount, VideoComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Posts.models import Post
from ProfileSite.models import  Specialty,SpecialtyType
from CinamaMedia.models import YouTube

# from Competition.models import MovieSections,Participants,JudgementComitys

# post

def DashboardVideo(request):
    userNav=request.user
    MyProfile = Channel.objects.get(slug=request.user)
    context = {
        "MyPro": MyProfile,
        "userNav":userNav

    }
    return render(request, "AdminProfile/MyVideo/index.html", context)

# Create your views here.
def base(request):
    return render(request, "AdminProfile/index.html")





def channel(request, slug):
    mychannel = Channel.objects.get(slug=slug)
    channel_videos = VideoFiles.objects.filter(channel=mychannel)
    context = {
        "channel": mychannel,
        "my_videos": channel_videos,

    }

    return render(request, "ProUser/myProfile.html", context)


def ChannelMyVideos(request, slug):
    mychannel = Channel.objects.get(slug=slug)
    channel_videos = VideoFiles.objects.filter(channel=mychannel)
    paginator = Paginator(channel_videos, 6)
    page = request.GET.get('page')
    try:
        channel_videos = paginator.page(page)
    except PageNotAnInteger:
        channel_videos = paginator.page(1)
    except EmptyPage:
        channel_videos = paginator.page(paginator.num_page)

    # mychannel=Channel.objects.get(slug=slug)
    # channel_videos=VideoFiles.objects.filter(channel=mychannel)
    context = {
        "channel": mychannel,
        "my_videos": channel_videos,
        'page': page,
    }

    return render(request, "AdminProfile/MyVideo/VideosProfile.html", context)

def ChannelMyVideosWeb(request):

    channel_videos = VideoFiles.objects.all()
    youTube = YouTube.objects.all()


    context = {

        "my_videos": channel_videos,
        "youTube":youTube,

    }

    return render(request, "Web/WebProfile/VideoWeb.html", context)

def ChannelMyVideosUserWeb(request,slug):

    MyProfile = Channel.objects.get(slug=slug)
    channel_videos = VideoFiles.objects.filter(channel=MyProfile)
    youTube = YouTube.objects.filter(author=MyProfile)


    context = {

        "my_videos": channel_videos,
        "youTube":youTube,
        "MyPro":MyProfile,

    }

    return render(request, "Web/UserProFile/VideoWeb.html", context)



def dashboard(request, slug):
    channel = get_object_or_404(Channel, slug=slug)
    myvideos = VideoFiles.objects.filter(channel=channel)
    context = {
        "channel": channel,
        "videos": myvideos

    }
    return render(request, "ProUser/DashVideo.html", context)

def delete_video(request, id):
    video = VideoFiles.objects.get(id=id)
    if request.method == "POST":
        video.delete()
        return redirect("ChannelMyVideos", slug=request.user.username)
    context = {
        "video": video
    }
    return render(request, "AdminProfile/MyVideo/Video_Delete.html",context)


def video_watch_view(request, video_id):
    user = request.user
    video = get_object_or_404(VideoFiles, id=video_id)
    vid_cat = video.channel.Specialty.Specialty
    suggested_videos = VideoFiles.objects.filter(channel__Specialty__Specialty=vid_cat).exclude(video=video.video)

    paginator = Paginator(suggested_videos, 4)
    page = request.GET.get('page')
    try:
        suggested_videos = paginator.page(page)
    except PageNotAnInteger:
        suggested_videos = paginator.page(1)
    except EmptyPage:
        suggested_videos = paginator.page(paginator.num_page)
    ip = request.META['REMOTE_ADDR']

    if not ViewCount.objects.filter(video=video, session=request.session.session_key):
        view = ViewCount(video=video, ip_address=ip, session=request.session.session_key)
        view.save()
    video_views = ViewCount.objects.filter(video=video).count()

    context = {
        "my_video": video,
        "view_count": video_views,
        "recommended_videos": suggested_videos,
        'page': page,
        'user':user

    }

    return render(request, "AdminProfile/MyVideo/Video_details.html", context)


@login_required
def liked_video(request, id):
    user = request.user
    Like = False
    if request.method == "POST":
        video_id = request.POST['video_id']
        get_video = get_object_or_404(VideoFiles, id=video_id)
        if user in get_video.likes.all():
            get_video.likes.remove(user)
            Like = False
        else:
            get_video.likes.add(user)
            Like = True
        data = {
            "liked": Like,
            "likes_count": get_video.likes.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect(reverse("video_watch", args=[str(id)]))


@login_required
def dislike_video(request, id):
    user = request.user
    Dislikes = False
    if request.method == "POST":
        video_id = request.POST['video_id']
        print("printing ajax id", video_id)
        watch = get_object_or_404(VideoFiles, id=video_id)
        if user in watch.dislikes.all():
            watch.dislikes.remove(user)
            Dislikes = False
        else:
            if user in watch.likes.all():
                watch.likes.remove(user)
            watch.dislikes.add(user)
            watch.save()
            Dislikes = True
        data = {
            "disliked": Dislikes,
            'dislike_count': watch.dislikes.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect(reverse("video_watch", args=[str(id)]))


@login_required
def subscriber_view(request):
    subscriber = request.user
    Subcribed = False
    if request.method == "POST":
        channel_id = request.POST['channel_id']
        channel = get_object_or_404(Channel, id=channel_id)
        if subscriber in channel.subcribers.all():
            channel.subcribers.remove(subscriber)
            Subcribed = False
        else:
            channel.subcribers.add(subscriber)
            channel.save()
            Subcribed = True
        data = {
            'Subscribed': Subcribed,
            'num_subscribers': channel.num_subcribers()
        }
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'an error has occured '})


@login_required
def video_comment(request, video_id):
    if request.method == "POST":
        comment = request.POST['comment']
        video = VideoFiles.objects.get(id=video_id)
        channel =Channel.objects.get(user=request.user)
        if comment is not None:
            create_comment = VideoComment(video=video, user=request.user,channel=channel, comment=comment)
            create_comment.save()
    return redirect('video_watch', video_id=video_id)




@login_required
def upload_view(request):
    return render(request, "AdminProfile/MyVideo/fileupload.html")



def upload_processing(request):
    user = request.user
    Profi = Channel.objects.get(user=user)

    if request.method == "POST":
        form = videoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            video = form.cleaned_data.get('video')
            desc = request.POST['description']
            visibility = request.POST['visibility']
            thumbnail = form.cleaned_data.get('thumbnail')

            VideoFiles.objects.create(video=video, channel=Profi,
                                title=title,description=desc, visibility=visibility, thumbnail=thumbnail
                                      )

        return redirect('ChannelMyVideos', user.username)

    form = videoForm()
    context = {
        "form": form,
    }
    return render(request, "AdminProfile/MyVideo/fileupload.html", context)

def upload_processingWeb(request,slug):
    MyProfile = get_object_or_404(Channel, slug=slug)
    user = request.user
    Profi = Channel.objects.get(user=user)

    if request.method == "POST":
        form = videoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            video = form.cleaned_data.get('video')
            desc = request.POST['description']
            visibility = request.POST['visibility']
            thumbnail = form.cleaned_data.get('thumbnail')

            VideoFiles.objects.create(video=video, channel=Profi,
                                title=title,description=desc, visibility=visibility, thumbnail=thumbnail
                                      )

        return redirect('ChannelMyVideosUserWeb', MyProfile.slug)

    form = videoForm()
    context = {
        "form": form,
        'MyPro':MyProfile
    }
    return render(request, "Web/UserProFile/info/AddVideo.html", context)




def Video_details(request, video_id):
    video = get_object_or_404(VideoFiles, id=video_id)
    vid_cat = video.channel.Specialty.Specialty
    suggested_videos = VideoFiles.objects.filter(channel__Specialty__Specialty=vid_cat).exclude(video=video.video)

    paginator = Paginator(suggested_videos, 4)
    page = request.GET.get('page')
    try:
        suggested_videos = paginator.page(page)
    except PageNotAnInteger:
        suggested_videos = paginator.page(1)
    except EmptyPage:
        suggested_videos = paginator.page(paginator.num_page)
    ip = request.META['REMOTE_ADDR']

    if not ViewCount.objects.filter(video=video, session=request.session.session_key):
        view = ViewCount(video=video, ip_address=ip, session=request.session.session_key)
        view.save()
    video_views = ViewCount.objects.filter(video=video).count()

    context = {
        "my_video": video,
        "view_count": video_views,
        "recommended_videos": suggested_videos,
        'page': page,

    }

    return render(request, 'AdminProfile/MyVideo/Video_details.html', context)


def VideodetailsWeb(request, video_id):
    video = get_object_or_404(VideoFiles, id=video_id)
    vid_cat = video.channel.Specialty.Specialty
    suggested_videos = VideoFiles.objects.filter(channel__Specialty__Specialty=vid_cat).exclude(video=video.video)

    paginator = Paginator(suggested_videos, 4)
    page = request.GET.get('page')
    try:
        suggested_videos = paginator.page(page)
    except PageNotAnInteger:
        suggested_videos = paginator.page(1)
    except EmptyPage:
        suggested_videos = paginator.page(paginator.num_page)
    ip = request.META['REMOTE_ADDR']

    if not ViewCount.objects.filter(video=video, session=request.session.session_key):
        view = ViewCount(video=video, ip_address=ip, session=request.session.session_key)
        view.save()
    video_views = ViewCount.objects.filter(video=video).count()

    context = {
        "my_video": video,
        "view_count": video_views,
        "recommended_videos": suggested_videos,
        'page': page,

    }

    return render(request, 'Web/WebProfile/VideoDietls.html', context)

@login_required
def videoWeb_comment(request, video_id):
    if request.method == "POST":
        comment = request.POST['comment']
        video = VideoFiles.objects.get(id=video_id)
        channel =Channel.objects.get(user=request.user)
        if comment is not None:
            create_comment = VideoComment(video=video, user=request.user,channel=channel, comment=comment)
            create_comment.save()
    return redirect('VideodetailsWeb', video_id=video_id)

class videoUpdate(LoginRequiredMixin, UpdateView):
    form_class = videoUpdateForm
    model = VideoFiles
    template_name = 'AdminProfile/MyVideo/Vodio_Update.html'


    def form_valid(self, form):
        profile = Channel.objects.get(user=self.request.user)
        if form.instance.channel == profile:

            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be the author of the post in order to update it")
            return super().form_invalid(form)

def AddVideo_Participants(request):
    user = request.user
    Profi = Channel.objects.get(user=user)




    if request.method == "POST":
        form = AddVideo_ParticipantsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            video = form.cleaned_data.get('video')
            desc = request.POST['description']
            Stages = form.cleaned_data.get('Stages')
            MovieSections = form.cleaned_data.get('MovieSections')
            visibility = request.POST['visibility']
            thumbnail = form.cleaned_data.get('thumbnail')

            VideoFiles.objects.create(video=video, channel=Profi,MovieSections=MovieSections,
                                title=title,description=desc, visibility=visibility, thumbnail=thumbnail,Stages=Stages
                                     )


        return redirect('MyParticipants')





    form = AddVideo_ParticipantsForm()
    context = {
        "form": form,

    }
    return render(request, "AdminProfile/Participants/AddVideo.html", context)

""""
def AddParticipant(request,video_id):
    video = get_object_or_404(VideoFiles, id=video_id)

    user = request.user
    Profi = Channel.objects.get(user=user)

    if request.method == "POST":

        form = AddParticipantForm(request.POST)
        p=Participant()
        if form.is_valid():
            p.title = 'title'
            p.video = video
            p.JudgementComity = video.channel.slug
            p.Participanted = video.channel.slug



            Participant.objects.create(title=p.title,video=p.video, user=Profi
                                      ,JudgementComity=p.JudgementComity, Participanted=p.Participanted)




        return redirect("MyParticipants")





    form = AddParticipantForm()
    context = {
        "form": form,
    }
    return render(request, "AdminProfile/Competitions/Participants/ParticipantsFormAdd.html", context)
"""
