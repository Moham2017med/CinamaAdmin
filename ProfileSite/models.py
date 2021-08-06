import uuid
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings

from googletrans import Translator

translator = Translator()







User = settings.AUTH_USER_MODEL

def ProfileWeb_Icon_path(instance, filename):
    return "Profile_Art/%Y%/%m/%d".format(instance.user.id, filename)

# Create your models here.


class SpecialtyType(models.Model):
    SpecialtyType = models.CharField(max_length=50, verbose_name="نوع التخصص")
    is_active     = models.BooleanField(default=False, verbose_name="الحالة")
    is_Site_1 = models.BooleanField(default=False, verbose_name="الهيئة العليا")
    is_Site_2 = models.BooleanField(default=False, verbose_name="الادارة")
    is_Site_3 = models.BooleanField(default=False, verbose_name="لجنة التحكيم")
    is_Site_4 = models.BooleanField(default=False, verbose_name="المشتركين")
    is_Site_5 = models.BooleanField(default=False, verbose_name="أعضاء التميز")

    class Meta:
        verbose_name = "نوع التخصص"
        verbose_name_plural = "نوع تخصص"

    def __str__(self):
        return self.SpecialtyType


class Specialty(models.Model):
    Specialty = models.CharField(max_length=50, verbose_name="نوع التخصص")
    SpecialtyType = models.ForeignKey(SpecialtyType, on_delete=models.CASCADE, null=True, verbose_name="التخصص")
    is_active = models.BooleanField(default=True, verbose_name="الحالة")
    is_Site_1 = models.BooleanField(default=False, verbose_name="قسم الاول")
    is_Site_2 = models.BooleanField(default=False, verbose_name="قسم الثاني")
    is_Site_3 = models.BooleanField(default=False, verbose_name="قسم الثالث")
    is_Site_4 = models.BooleanField(default=False, verbose_name="قسم الرابع")
    is_Site_5 = models.BooleanField(default=False, verbose_name="قسم الخامس")

    class Meta:
        verbose_name = "التخصص"
        verbose_name_plural = "التخصص"

    def __str__(self):
        return self.Specialty



class States(models.Model):
    State = models.CharField(max_length=50, verbose_name="الدولة")
    is_active = models.BooleanField(default=False, verbose_name="الحالة")

    class Meta:
        verbose_name = "الدول"
        verbose_name_plural = "الدول"

    def __str__(self):
        return self.State




class Profile(models.Model):

    FullName = models.CharField(blank=True, null=True,max_length=200, verbose_name="الاسم الكامل")
    State = models.ForeignKey(States, on_delete=models.CASCADE, blank=True, null=True, verbose_name="الدولة")
    age  = models.BooleanField(choices=((False, "لا ـ No"),(True, "نعم ـ Yes")),help_text="greater than 18", verbose_name="فئة أكبر من 18")
    DateOfBirth = models.DateField(blank=True, null=True, verbose_name="تاريخ الميلاد")
    gender = models.BooleanField(choices=((False, "ذكر ـ man"), (True, "انثى ـ female")),help_text="What is the gender?", verbose_name="نوع الجنس")
    SpecialtyType = models.ForeignKey(SpecialtyType, on_delete=models.CASCADE, blank=True, null=True, verbose_name="نوع التخصص")
    Specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=True, null=True, verbose_name="التخصص")
    Phone = models.CharField(max_length=100,null=True, blank=True, verbose_name="رقم الجوال")
    Profile_Art = models.ImageField(upload_to="Profile_Art/%Y%/%m/%d/", default='default_art.jpg', verbose_name="صورة ويب")
    Profile_Icon = models.ImageField(upload_to='Profile_Icon/%Y/%m/%d/', default='default_icon.png', verbose_name="صورة المستخدم")
    description = models.TextField(blank=True, null=True, verbose_name="نبدا عنك")
    address = models.TextField(blank=True, null=True, verbose_name="عنوان الاقامة")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,verbose_name="أسم المستخدم")
    slug = models.SlugField(verbose_name="id" ,blank=True, null=True)
    subcribers = models.ManyToManyField(User, blank=True, related_name="subscribers", verbose_name="المشتركين")
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    emaiAddress=models.EmailField(blank=True, null=True,verbose_name="البريد الكتروني")
    date_joined = models.DateTimeField(verbose_name="تاريخ التسجيل", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="تاريخ الدخول", auto_now=True)
    Facebook = models.CharField(max_length=500, blank=True, null=True, verbose_name="الفيس بوك")
    Instagram = models.CharField(max_length=500, blank=True, null=True, verbose_name="انستقرام")
    Twitter = models.CharField(max_length=500, blank=True, null=True, verbose_name="تويتر")
    Snapchat = models.CharField(max_length=500, blank=True, null=True, verbose_name="سناب شات")
    YouTube = models.CharField(max_length=500, blank=True, null=True, verbose_name="اليوتيوب")
    Skype = models.CharField(max_length=500, blank=True, null=True, verbose_name="سكاي بي")
    Zoom = models.CharField(max_length=500, blank=True, null=True, verbose_name="زوم")
    is_active = models.BooleanField(default=True, verbose_name="المستخدم")
    is_subcriber = models.BooleanField(default=False, verbose_name="مشترك")
    is_supersubcriber = models.BooleanField(default=False, verbose_name="للجنة التحكيم")
    is_admin = models.BooleanField(default=False, verbose_name="المدير")
    is_staff = models.BooleanField(default=False, verbose_name="التميز")
    is_star = models.BooleanField(default=False, verbose_name="نجمة")
    is_Media = models.BooleanField(default=False, verbose_name="مواقع تواصل الاجتماعي")
    is_Posts = models.BooleanField(default=False, verbose_name="منشورات")
    is_YouTube = models.BooleanField(default=False, verbose_name="اليوتيوب")
    is_Video = models.BooleanField(default=False, verbose_name="فيديوهات")
    is_Articles = models.BooleanField(default=False, verbose_name="مقالات")


    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملف الشخصي"

    def __str__(self):
        return f'{self.user.username}'

    def num_subcribers(self):
        return self.subcribers.count()










