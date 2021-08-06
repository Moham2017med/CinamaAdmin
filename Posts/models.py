from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from ProfileSite.models import Profile



class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='author',verbose_name='الكاتب')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='profile', verbose_name='المستخدم')
    liked = models.ManyToManyField(User, default=None, blank=True, verbose_name='أعجاب')
    image = models.ImageField(blank=True, null=True , upload_to='post_pic/%Y%/%m/%d/',verbose_name='صورة المنشور')
    caption  = models.TextField(max_length=500,verbose_name=' المنشور')
    created_date = models.DateTimeField(default=timezone.now,verbose_name='تاريخ المنشور')
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True,verbose_name='حفظ المنشور')
    imageVideo = models.ImageField(blank=True, null=True, upload_to='video_posts/imageVideo/%Y%/%m/%d/',verbose_name='صورة عرض')
    video = models.FileField(upload_to='video_posts/%Y%/%m/%d/', null=True, blank=True,verbose_name='تحميل الفيديو')
    is_active = models.BooleanField(default=True, verbose_name="موافقة نشر")
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # who sent the request
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')  # who will receive the request
    # sender = models.CharField(max_length=20, default='requested')
    status = models.CharField(max_length=20, default='requested')
    created_at = models.DateTimeField(default=now)




class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment')
    comment_updated = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk':self.pk})


#############################################

FAV_CHOICES = (
    ('Save', 'Save'),
    ('Saved', 'Saved')
)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=FAV_CHOICES, default='Save', max_length=10)

    def __str__(self):
        return str(self.post)
