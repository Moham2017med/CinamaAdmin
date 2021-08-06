from django.urls import path
from . import views
from . views import *


urlpatterns = [



    path('DashboardPosts/',views.DashboardPosts, name='DashboardPosts'),
    path('like_post', views.like_post, name='like_post'),
    path('like_postWeb', views.like_postWeb, name='like_postWeb'),


    path('profile/<slug>/', views.profile, name='profile'),



    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/',PostDetailView, name='post_details'),
    path('post/<int:pk>/delete/',PostDeleteview.as_view(), name='post_delete' ),
    
    path('profile_posts',views.profile_posts, name='profile_posts'),
    path('results',views.results, name='results'),
    path('post/new/',PostCreateView, name='post-create' ),

    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update' ),

    


    path('delete/<int:id>',views.delete, name='delete'),

    path('favourite',views.favourite, name='favourite'),
    path('favourite_posts',views.favourite_posts, name='favourite_posts'),

    path('video/new/',VideoCreateView, name='video-create' ),
    path('post/<int:pk>/video',video_update.as_view(), name='video_update' ),

    # path('<str:username>',views.userprofile, name='userprofile'),
    path('video_posts',views.video_posts, name='video_posts'),

    path('user_videos',views.user_videos,name='user_videos'),

    path('PostDetailViewWeb/<int:pk>/',PostDetailViewWeb, name='PostDetailViewWeb'),
    path('postsWeb',views.postsWeb, name='postsWeb'),

    path('postsUserWeb/<slug>/', views.postsUserWeb, name='postsUserWeb'),
    path('PostCreateViewWeb/<slug>/', views.PostCreateViewWeb, name='PostCreateViewWeb'),
    path('VideoCreateViewWeb/<slug>/', views.VideoCreateViewWeb, name='VideoCreateViewWeb'),




    
    


]

