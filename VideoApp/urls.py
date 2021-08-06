from django.urls import path
from .views import (
                    channel,
Video_details,
videoUpdate,
DashboardVideo,
AddVideo_Participants,



                    upload_processing,

                    video_watch_view,
                    liked_video,
                    dislike_video,
                    subscriber_view,
                    video_comment,
                    dashboard,
                    delete_video,
                    ChannelMyVideos,
                    base,
VideodetailsWeb,
videoWeb_comment,
ChannelMyVideosWeb,
ChannelMyVideosUserWeb,
upload_processingWeb,
                   )


urlpatterns=[
    path('base/', base, name="base"),
    path('DashboardVideo/', DashboardVideo, name="DashboardVideo"),
    path("watch/?v=<uuid:video_id>", video_watch_view, name="video_watch"),
    path("channel/<slug>/", channel, name="mychannel"),
    path("ChannelMyVideos/<slug>/", ChannelMyVideos, name="ChannelMyVideos"),
    path("channel/dashboard/<slug>/", dashboard, name="channel-dashboard"),
    path("like/<uuid:id>/", liked_video, name="like-video"),
    path("channel/delete_video/<uuid:id>", delete_video, name="delete-video"),
    path("dislike/<uuid:id>/", dislike_video, name="dislike-video"),

    path("upload/", upload_processing, name="file-upload"),

    path("subscribe/", subscriber_view, name="subscriber"),
    path("user_comment/<uuid:video_id>", video_comment, name="comment"),

    path("Video_details/?v=<uuid:video_id>", Video_details, name="Video_details"),
    path('<pk>/videoUpdate/', videoUpdate.as_view(), name='videoUpdate'),

    path("AddVideo/", AddVideo_Participants, name="AddVideo_Participants"),
    path("VideodetailsWeb/?v=<uuid:video_id>", VideodetailsWeb, name="VideodetailsWeb"),
    path("videoWeb_comment/<uuid:video_id>", videoWeb_comment, name="videoWeb_comment"),

    path("ChannelMyVideosWeb/", ChannelMyVideosWeb, name="ChannelMyVideosWeb"),
    path('ChannelMyVideosUserWeb/<slug>/', ChannelMyVideosUserWeb, name='ChannelMyVideosUserWeb'),
    path('upload_processingWeb/<slug>/', upload_processingWeb, name='upload_processingWeb'),


]