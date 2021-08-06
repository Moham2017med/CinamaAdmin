from django.urls import path
from .views import *


urlpatterns=[
    path('', indexHome, name="home"),
    path('CompetitionsWeb', CompetitionsWeb, name="CompetitionsWeb"),
    path('WhoAreWeWeb', WhoAreWeWeb, name="WhoAreWeWeb"),
    path('DashboardPro', DashboardPro, name="DashboardPro"),
    path('MyWerk/', ProfileViwe, name="ProfileViwe"),
    path('MyProfile/<slug>/', MyProfile, name="MyProfile"),
    path("ProfileInfo/", WebProfileWeb_info, name="ProfileInfo"),
    path('find_friends/<slug>/',find_friends, name='find_friends'),
    path('friends/<slug>/', friends, name='friends'),
    path("VideoDetails/?v=<uuid:video_id>", VideoDetails, name="VideoDetails"),

    path("indexPostsWeb/<int:id>/", indexPostsWeb, name="indexPostsWeb"),
    path('indexHomeUser/<slug>/', indexHomeUser, name="indexHomeUser"),






]
