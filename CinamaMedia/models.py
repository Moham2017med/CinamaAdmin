from django.db import models
from django.core.validators import FileExtensionValidator
from ProfileSite.models import  Profile
# Create your models here.

class YouTubeTypes(models.Model):
    YouTubeType = models.CharField(max_length=50, verbose_name="قسم الفيديو")
    is_Site_1 = models.BooleanField(default=False, verbose_name="قسم الاول")
    is_Site_2 = models.BooleanField(default=False, verbose_name="قسم الثاني")
    is_Site_3 = models.BooleanField(default=False, verbose_name="قسم الثالث")
    is_Site_4 = models.BooleanField(default=False, verbose_name="قسم الرابع")
    is_Site_5 = models.BooleanField(default=False, verbose_name="قسم الخامس")
    class Meta:
       verbose_name = "أقسام الفيديوهات"
       verbose_name_plural = "أقسام الفيديوهات"
    def __str__(self):
        return self.YouTubeType


class YouTube(models.Model):

    title=models.CharField(max_length=200, verbose_name="العنوان")
    YouTubeType = models.ForeignKey(YouTubeTypes, on_delete=models.CASCADE, null=True, verbose_name="نوع التخصص")

    linke = models.TextField(verbose_name="رابط الفيديو")
    content = models.TextField(verbose_name="وصف الفيديو")
    image = models.ImageField(upload_to='youTube/%Y%/%m/%d/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
                              blank=True,verbose_name="رفع الصورة")
    updated = models.DateTimeField(auto_now=True,verbose_name="تتاريخ التحديث")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاريخ التتسجيل")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='YouTubs',verbose_name="أسم المستخدم")
    is_active = models.BooleanField(default=True, verbose_name="موافقة نشر")
    is_admin = models.BooleanField(default=False, verbose_name="الادارة")
    is_staff = models.BooleanField(default=False, verbose_name="التميز")


    class Meta:
       verbose_name = "الفيديوهات"
       verbose_name_plural = "الفيديوهات"

    def __str__(self):
        return self.title

class LecturesTypes(models.Model):
    LecturesType = models.CharField(max_length=50, verbose_name="قسم الفيديو")
    is_Site_1 = models.BooleanField(default=False, verbose_name="قسم الاول")
    is_Site_2 = models.BooleanField(default=False, verbose_name="قسم الثاني")
    is_Site_3 = models.BooleanField(default=False, verbose_name="قسم الثالث")
    is_Site_4 = models.BooleanField(default=False, verbose_name="قسم الرابع")
    is_Site_5 = models.BooleanField(default=False, verbose_name="قسم الخامس")
    class Meta:
       verbose_name = "نواع المحاضرات"
       verbose_name_plural = "نواع المحاضرات"
    def __str__(self):
        return self.LecturesType


class Lectures(models.Model):

    title=models.CharField(max_length=200, verbose_name="العنوان")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='Lectures', verbose_name="أسم المحاضر")
    LecturesType = models.ForeignKey(LecturesTypes, on_delete=models.CASCADE, null=True, verbose_name="نوع المحاضرة")
    linke = models.TextField(verbose_name="رابط المحاضرة")
    content = models.TextField(verbose_name="وصف المحاضرة")
    image = models.ImageField(upload_to='Lectures/%Y%/%m/%d/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
                              blank=True,verbose_name="رفع الصورة")
    Date = models.DateTimeField( verbose_name="تاريخ المحاضرة")
    Time = models.TimeField( verbose_name="وقت المحاضرة")
    updated = models.DateTimeField(auto_now=True,verbose_name="تتاريخ التحديث")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاريخ التتسجيل")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='Lecturesauthor',verbose_name="أسم المستخدم")
    is_active = models.BooleanField(default=True, verbose_name="موافقة نشر")
    is_admin = models.BooleanField(default=False, verbose_name="الادارة")
    is_staff = models.BooleanField(default=False, verbose_name="التميز")


    class Meta:
       verbose_name = "المحاضرات"
       verbose_name_plural = "المحاضرات"

    def __str__(self):
        return self.title

class CinamaMedias(models.Model):
    title=models.CharField(max_length=200, verbose_name="العنوان")
    Facebook = models.CharField(max_length=500, blank=True, null=True, verbose_name="الفيس بوك")
    Instagram = models.CharField(max_length=500, blank=True, null=True, verbose_name="انستقرام")
    Twitter = models.CharField(max_length=500, blank=True, null=True, verbose_name="تويتر")
    Snapchat = models.CharField(max_length=500, blank=True, null=True, verbose_name="سناب شات")
    YouTube = models.CharField(max_length=500, blank=True, null=True, verbose_name="اليوتيوب")
    class Meta:
       verbose_name = "موقع تتواصل المهرجان"
       verbose_name_plural = "موقع تتواصل المهرجان"
    def __str__(self):
        return self.title

