from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Friend, Comment, Favourites

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User, auth
from ProfileSite.models import Profile

################################################
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCreateForm,videoCreateForm

def DashboardPosts(request):
    userNav=request.user
    MyProfile = Profile.objects.get(slug=request.user)
    context = {
        "MyPro": MyProfile,
        "userNav":userNav

    }
    return render(request, "AdminProfile/MyPosts/index.html", context)

def PostsInfo(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    context = {
        "MyPro": MyProfile,
      }
    return render(request, 'AdminProfile/MyPosts/MunePosts.html', context)

####################################################

def index(request):
    posts = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    user = request.user
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, 'AdminProfile/MyPosts/index.html', context)



# for index likes

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_post = Post.objects.get(id=post_id)

        if user in post_post.liked.all():
            post_post.liked.remove(user)
        else:
            post_post.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('post_details',post_id)

def like_postWeb(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_post = Post.objects.get(id=post_id)

        if user in post_post.liked.all():
            post_post.liked.remove(user)
        else:
            post_post.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('PostDetailViewWeb',post_id)



#############################################

# profile page

def profile(request, slug):
    MyProfile = Profile.objects.get(slug=slug)
    context = {
        "MyPro": MyProfile,
      }
    return render(request, 'AdminProfile/MyPosts/MunePosts.html', context)






################################
# individual user posts

class UserPostListView(ListView):
    model = Post
    template_name = 'AdminProfile/MyPosts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created_date')


################################
# post details page

def PostDetailView(request,pk):
    user = request.user
    posts = Post.objects.get(id=pk)
    Commen =Comment.objects.filter(post_connected=posts)

    if request.method =="POST":
        content=request.POST['content']
        post = Post.objects.get(id=pk)
        if content is not None:
            create_comment=Comment(post_connected=post, author=request.user, content=content)
            create_comment.save()

        return redirect('post_details', pk=pk)

    return render(request, 'AdminProfile/MyPosts/post_details.html', {'posts': posts, 'user': user,'Commen':Commen})


def PostDetailViewWeb(request,pk):
    user = request.user
    posts = Post.objects.get(id=pk)
    Commen =Comment.objects.filter(post_connected=posts)

    if request.method =="POST":
        content=request.POST['content']
        post = Post.objects.get(id=pk)
        if content is not None:
            create_comment=Comment(post_connected=post, author=request.user, content=content)
            create_comment.save()

        return redirect('PostDetailViewWeb', pk=pk)

    return render(request, 'Web/WebProfile/PostsDietls.html', {'posts': posts, 'user': user,'Commen':Commen})



class PostDeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/Posts/profile_posts'
    template_name = 'AdminProfile/MyPosts/post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def PostCreateView(request):

    u = Post
    user=request.user
    Profi=Profile.objects.get(user=user)

    if request.method =="POST":
        form=PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')


            Post.objects.create(image=image, author=user,profile=Profi,
                                   caption=caption)


        return redirect("profile_posts")

    form=PostCreateForm()
    context={
     "form":form,
    }
    return render(request, "AdminProfile/MyPosts/post_form.html", context)

def PostCreateViewWeb(request,slug):
    MyProfile = Profile.objects.get(slug=slug)

    u = Post
    user=request.user
    Profi=Profile.objects.get(user=user)

    if request.method =="POST":
        form=PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')


            Post.objects.create(image=image, author=user,profile=Profi,
                                   caption=caption)


        return redirect("postsUserWeb", MyProfile.slug)

    form=PostCreateForm()
    context={
     "form":form,
     'MyPro':MyProfile
    }
    return render(request, "Web/UserProFile/info/AddPost.html", context)



############################
# for post update

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = '/Posts/profile_posts'
    template_name = 'AdminProfile/MyPosts/post_update.html'
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

    posts = Post.objects.filter(author=request.user).order_by('-created_date')


    return render(request, 'AdminProfile/MyPosts/profile_posts.html', {'posts': posts, 'user': user})

def postsWeb(request):
    user = request.user

    posts = Post.objects.all().order_by('-created_date')


    return render(request, 'Web/WebProfile/PostsWeb.html', {'posts': posts, 'user': user})

def postsUserWeb(request,slug):
    user = request.user
    MyProfile=Profile.objects.get(slug=slug)
    posts = Post.objects.filter(profile=MyProfile).order_by('-created_date')


    return render(request, 'Web/UserProFile/PostsWeb.html', {'posts': posts,"MyPro":MyProfile, 'user': user})
#####################################
# search function

def results(request):  # multiple search
    if request.method == 'GET':
        srch = request.GET.get('srh')


        if srch:
            users = User.objects.filter(Q(username__icontains=srch) | Q(email__icontains=srch))

            if users:
                return render(request, 'AdminProfile/MyPosts/results.html', {'users': users, })
            else:
                # messages.error(request,"No similar results for")
                messages.error(request, srch)
        else:

            return render(request, 'AdminProfile/MyPosts/results.html')
    return render(request, 'AdminProfile/MyPosts/results.html')


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
        post_post = Post.objects.get(id=post_id)

        if user in post_post.favourite.all():
            post_post.favourite.remove(user)
        else:
            post_post.favourite.add(user)
        Fav, created = Favourites.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if Fav.value == 'Save':
                Fav.value = 'Saved'
            else:
                Fav.value = 'Save'
        Fav.save()
    return redirect('favourite_posts')


#################################
# template for favourite posts

def favourite_posts(request):
    user = request.user
    num_count = user.favourite.filter().count()
    favourite_posts = user.favourite.all().order_by('-created_date')
    context = {
        'favourite_posts': favourite_posts,
        'num_count': num_count
    }

    return render(request, 'AdminProfile/MyPosts/favourite_posts.html', context)


#########################################
# video Post

def VideoCreateView(request):
    u = Post
    user = request.user
    Profi = Profile.objects.get(user=user)

    if request.method == "POST":
        form = videoCreateForm(request.POST, request.FILES)
        if form.is_valid():

            video = form.cleaned_data.get('video')
            imageVideo = form.cleaned_data.get('imageVideo')
            caption = form.cleaned_data.get('caption')

            Post.objects.create(video=video,imageVideo=imageVideo, author=user, profile=Profi,
                                caption=caption)

        return redirect("profile_posts")

    form = videoCreateForm()
    context = {
        "form": form,
    }
    return render(request, "AdminProfile/MyPosts/video_form.html", context)

def VideoCreateViewWeb(request,slug):
    MyProfile = Profile.objects.get(slug=slug)
    u = Post
    user = request.user
    Profi = Profile.objects.get(user=user)

    if request.method == "POST":
        form = videoCreateForm(request.POST, request.FILES)
        if form.is_valid():

            video = form.cleaned_data.get('video')
            imageVideo = form.cleaned_data.get('imageVideo')
            caption = form.cleaned_data.get('caption')

            Post.objects.create(video=video,imageVideo=imageVideo, author=user, profile=Profi,
                                caption=caption)

        return redirect("postsUserWeb", MyProfile.slug)

    form = videoCreateForm()
    context = {
        "form": form,
        'MyPro': MyProfile
    }
    return render(request, "Web/UserProFile/info/AddVideoPost.html", context)


#########################################
# Update video Post

class video_update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = '/Posts/profile_posts'
    template_name = 'AdminProfile/MyPosts/video_update.html'
    fields = ['video', 'caption','imageVideo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def video_posts(request):
    posts = Post.objects.all().order_by('?')[:40]
    context = {
        'posts': posts,
    }
    return render(request, 'AdminProfile/MyPosts/video_posts.html', context)


def user_videos(request):
    user = request.user

    posts = Post.objects.filter(author=request.user).order_by('-created_date')
    return render(request, 'user_videos.html', {'posts': posts, 'user': user})


