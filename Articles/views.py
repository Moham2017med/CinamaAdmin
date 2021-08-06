from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.contrib import messages

from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User, auth
from ProfileSite.models import Profile

################################################
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *

def DashboardArticles(request):
    userNav=request.user
    MyProfile = Profile.objects.get(slug=request.user)
    context = {
        "MyPro": MyProfile,
        "userNav":userNav

    }
    return render(request, "AdminProfile/Articles/index.html", context)

def PostsInfo(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    context = {
        "MyPro": MyProfile,
      }
    return render(request, 'AdminProfile/Articles/MunePosts.html', context)

####################################################

def index(request):
    posts = Articles.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    user = request.user
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, 'AdminProfile/Articles/index.html', context)



# for index likes

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_post = Articles.objects.get(id=post_id)

        if user in post_post.liked.all():
            post_post.liked.remove(user)
        else:
            post_post.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, Articles_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('post_detailsArticles', post_id)
#############################################
def like_ArticlesWeb(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_post = Articles.objects.get(id=post_id)

        if user in post_post.liked.all():
            post_post.liked.remove(user)
        else:
            post_post.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, Articles_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('ArticlesDetailViewWeb', post_id)
# profile page

def profile(request, slug):
    MyProfile = Profile.objects.get(slug=slug)
    context = {
        "MyPro": MyProfile,
      }
    return render(request, 'AdminProfile/Articles/MunePosts.html', context)






################################
# individual user posts

class UserPostListView(ListView):
    model = Articles
    template_name = 'AdminProfile/Articles/index.html'
    context_object_name = 'postsArticles'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Articles.objects.filter(author=user).order_by('-created_date')


################################
# post details page

def PostDetailView(request,pk):
    user = request.user
    posts = Articles.objects.get(id=pk)
    Commen =Comment.objects.filter(post_connected=posts)

    if request.method =="POST":
        content=request.POST['content']
        post = Articles.objects.get(id=pk)
        if content is not None:
            create_comment=Comment(post_connected=post, author=request.user, content=content)
            create_comment.save()

        return redirect('post_detailsArticles', pk=pk)

    return render(request, 'AdminProfile/Articles/post_details.html', {'posts': posts, 'user': user,'Commen':Commen})

def ArticlesDetailViewWeb(request,pk):
    user = request.user
    posts = Articles.objects.get(id=pk)
    Commen =Comment.objects.filter(post_connected=posts)

    if request.method =="POST":
        content=request.POST['content']
        post = Articles.objects.get(id=pk)
        if content is not None:
            create_comment=Comment(post_connected=post, author=request.user, content=content)
            create_comment.save()

        return redirect('ArticlesDetailViewWeb', pk=pk)

    return render(request, 'Web/WebProfile/ArticlesDietls.html', {'posts': posts, 'user': user,'Commen':Commen})


#############################
# for delete post

class PostDeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    success_url = '/Posts/profile_posts'
    template_name = 'AdminProfile/MyPosts/post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def PostCreateView(request):

    u = Articles
    user=request.user
    Profi=Profile.objects.get(user=user)

    if request.method =="POST":
        form=ArticlesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')


            Articles.objects.create(image=image, author=user,profile=Profi,
                                   caption=caption,title=title)


        return redirect("profile_postsArticles")

    form=ArticlesCreateForm()
    context={
     "form":form,
    }
    return render(request, "AdminProfile/Articles/post_form.html", context)

def ArticlesCreateViewWeb(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    u = Articles
    user=request.user
    Profi=Profile.objects.get(user=user)

    if request.method =="POST":
        form=ArticlesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')


            Articles.objects.create(image=image, author=user,profile=Profi,
                                   caption=caption,title=title)


        return redirect('ArticlesUserWeb', MyProfile.slug)

    form=ArticlesCreateForm()
    context={
     "form":form,
        'MyPro':MyProfile
    }
    return render(request, "Web/UserProFile/info/AddArticles.html", context)




############################
# for post update

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    success_url = '/Posts/profile_posts'
    template_name = 'AdminProfile/Articles/post_update.html'
    fields = ['image', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


############################
# profile posts

def profile_posts(request):
    user = request.user

    posts = Articles.objects.filter(author=request.user).order_by('-created_date')


    return render(request, 'AdminProfile/Articles/profile_posts.html', {'posts': posts, 'user': user})

def ArticlesWeb(request):
    user = request.user

    posts = Articles.objects.all().order_by('-created_date')


    return render(request, 'Web/WebProfile/ArticlesWeb.html', {'posts': posts, 'user': user})

def ArticlesUserWeb(request,slug):
    user = request.user
    MyProfile=Profile.objects.get(slug=slug)
    posts = Articles.objects.filter(profile=MyProfile).order_by('-created_date')


    return render(request, 'Web/UserProFile/ArticlesWeb.html', {'posts': posts,"MyPro":MyProfile, 'user': user})



#####################################
# search function

def results(request):  # multiple search
    if request.method == 'GET':
        srch = request.GET.get('srh')


        if srch:
            users = User.objects.filter(Q(username__icontains=srch) | Q(email__icontains=srch))

            if users:
                return render(request, 'AdminProfile/Articles/results.html', {'users': users, })
            else:
                # messages.error(request,"No similar results for")
                messages.error(request, srch)
        else:

            return render(request, 'AdminProfile/Articles/results.html')
    return render(request, 'AdminProfile/Articles/results.html')


#######################
# comments update




###########################
# comment delete

def delete(request, id):
    comments = Comment.objects.get(id=id).delete()
    messages.info(request, 'comment deleted')
    return redirect('/index')


#########################
# User Favourite posts

def favourite(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_post = Articles.objects.get(id=post_id)

        if user in post_post.favourite.all():
            post_post.favourite.remove(user)
        else:
            post_post.favourite.add(user)
        Fav, created = Favourites.objects.get_or_create(user=user, Articles_id=post_id)
        if not created:
            if Fav.value == 'Save':
                Fav.value = 'Saved'
            else:
                Fav.value = 'Save'
        Fav.save()
    return redirect('profile_postsArticles')


#################################
# template for favourite posts

def favourite_post(request):
    user = request.user
    num_count = user.FavouritesUser.filter().count()
    favourite_posts = user.FavouritesUser.all()
    context = {
        'favourite_posts': favourite_posts,
        'num_count': num_count
    }

    return render(request, 'AdminProfile/Articles/favourite_posts.html', context)


#########################################
# video Post



#########################################
# Update video Post




