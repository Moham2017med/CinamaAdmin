from django.urls import path
from .views import *


                    



urlpatterns=[
    path('DashboardCinamaMedia/', DashboardCinamaMedia, name="DashboardCinamaMedia"),
    path('AddYouTube/', AddYouTube, name="AddYouTube"),
    path("YouTubeProfile/", YouTubeProfile, name="YouTubeProfile"),
    path('YouTubeDelete/<int:id>/',YouTubeDelete, name='YouTubeDelete' ),
    path('<pk>/YouTubeUpdate/', YouTubeUpdateView.as_view(), name='YouTubeUpdate'),
    path('LecturesViwe/', LecturesViwe, name="LecturesViwe"),
    path('AddYouTubeWeb/<slug>/', AddYouTubeWeb, name="AddYouTubeWeb"),
    path('LecturesUserViwe/<slug>/', LecturesUserViwe, name="LecturesUserViwe"),



]
