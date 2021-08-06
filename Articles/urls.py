from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('DashboardArticles/', views.DashboardArticles, name='DashboardArticles'),
    path('like_post/', views.like_post, name='like_postArticles'),

    path('profile/<slug>/', views.profile, name='profileArticles'),

    path('user/<str:username>', UserPostListView.as_view(), name='user_postsArticles'),
    path('post/<int:pk>/', PostDetailView, name='post_detailsArticles'),
    path('post/<int:pk>/delete/', PostDeleteview.as_view(), name='post_deleteArticles'),

    path('profile_posts', views.profile_posts, name='profile_postsArticles'),
    path('results', views.results, name='resultsArticles'),
    path('post/new/', PostCreateView, name='post-createArticles'),

    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-updateArticles'),

    path('delete/<int:id>', views.delete, name='deleteArticles'),

    path('favourite', views.favourite, name='favouriteArticles'),
    path('favourite_posts/', views.favourite_post, name='favourite_postsArticles'),

    path('ArticlesDetailViewWeb/<int:pk>/', ArticlesDetailViewWeb, name='ArticlesDetailViewWeb'),
    path('like_ArticlesWeb/', views.like_ArticlesWeb, name='like_ArticlesWeb'),
    path('ArticlesWeb/', views.ArticlesWeb, name='ArticlesWeb'),
    path('ArticlesUserWeb/<slug>/', views.ArticlesUserWeb, name='ArticlesUserWeb'),
    path('ArticlesCreateViewWeb/<slug>/', views.ArticlesCreateViewWeb, name='ArticlesCreateViewWeb'),




]

