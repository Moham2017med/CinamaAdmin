from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from ProfileSite.models import Profile
from ckeditor.fields import RichTextField



class Articles(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='authorArticles')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ProfileArticles')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='likedArticles')
    image = models.ImageField(blank=True, null=True, upload_to='Articles_pic/%Y%/%m/%d/')
    caption  = RichTextField( blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updatedArticles = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    favourite = models.ManyToManyField(User, related_name='favouriteArticles', blank=True)
    is_active = models.BooleanField(default=False, verbose_name="موافقة نشر")
    is_admin = models.BooleanField(default=False, verbose_name="المدير")
    is_staff = models.BooleanField(default=False, verbose_name="التميز")
    is_Site_1 = models.BooleanField(default=False, verbose_name="قسم الاول")
    is_Site_2 = models.BooleanField(default=False, verbose_name="قسم الثاني")
    is_Site_3 = models.BooleanField(default=False, verbose_name="قسم الثالث")
    is_Site_4 = models.BooleanField(default=False, verbose_name="قسم الرابع")
    is_Site_5 = models.BooleanField(default=False, verbose_name="قسم الخامس")


    def __str__(self):
        return self.caption

    @property
    def num_favourites(self):
        return self.favourite.all().count()

    @property
    def num_likes(self):
        return self.liked.all().count()

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk':self.pk})
#############################################
LIKE_CHOICES =(
    ('Like','Like'),
    ('Unlike','Unlike')

)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='likedUser')
    Articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.Articles)




class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='CommentUser')
    post_connected = models.ForeignKey(Articles, on_delete=models.CASCADE,related_name='commentArticles')
    comment_updated = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk':self.pk})


#############################################

FAV_CHOICES = (
    ('Save', 'Save'),
    ('Saved', 'Saved')
)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='FavouritesUser')
    Articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    value = models.CharField(choices=FAV_CHOICES, default='Save', max_length=10)

    def __str__(self):
        return str(self.Articles)

