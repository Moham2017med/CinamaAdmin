from django.urls import path
from .views import *


                    



urlpatterns=[

    path('JudgementComitysView/<int:id>/', JudgementComitysView, name="JudgementComitysView"),
    path('ParticipantsView/<int:id>/', ParticipantsView, name="ParticipantsView"),
    path('AddComitys/<slug>/<uuid:video_id>/', AddComitys, name='AddComitys'),
    path('MyParticipants/', MyParticipants, name="MyParticipants"),
    path('JudMyParticipantsView/<uuid:video_id>/', JudgementyMyParticipantsView, name="JudMyParticipantsView"),
    path('JudgementComitysPartView/<uuid:video_id>/', JudgementComitysPartView, name="JudgementComitysPartView"),
    path('JudgementComitysViewWeb/<int:id>/', JudgementComitysViewWeb, name="JudgementComitysViewWeb"),
    path('JudgementComitysUserView/<slug>/', JudgementComitysUserView, name="JudgementComitysUserView"),
    path('JudgementComitysUserVideos/?v=<uuid:video_id>/', JudgementComitysUserVideos, name="JudgementComitysUserVideos"),

    path('JudgementComitysViewWebHome/<int:id_M>/', JudgementComitysViewWebHome, name="JudgementComitysViewWebHome"),



]
