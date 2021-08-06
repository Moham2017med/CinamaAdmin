from django.db import models

from ProfileSite.models import Profile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from VideoApp.models import *




class JudgementComitys(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="الاسم")
    video = models.ForeignKey(VideoFiles, on_delete=models.CASCADE,blank=True,null=True, verbose_name="الفيديو")
    Section = models.ForeignKey(Sections, on_delete=models.CASCADE,default=1, verbose_name="الموسم")
    Stages = models.ForeignKey(Stages, on_delete=models.CASCADE, verbose_name="مراحل المسابقة")
    MovieSections = models.ForeignKey(MovieSection, on_delete=models.CASCADE, verbose_name="قسم المسابقة")
    JudgementComity = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="لجنة التحكيم")
    description = models.TextField( blank=True,null=True,verbose_name="من انا")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="أسم المستخدم")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التتسجيل")
    is_log = models.BooleanField(default=True, verbose_name="تسجيل")
    is_approval = models.BooleanField(default=True, verbose_name="موافقة")
    is_active = models.BooleanField(default=True, verbose_name="موافقة نشر")
    is_admin = models.BooleanField(default=False, verbose_name="لجنة التحكيم")
    is_staff = models.BooleanField(default=False, verbose_name="انتهاء")

    class Meta:
        verbose_name = "تحكيم المتسابقين"
        verbose_name_plural = "تحكيم المتسابقين"

    def __str__(self):
        return self.title

class JudgementRacer(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="الاسم")
    video = models.ForeignKey(VideoFiles, on_delete=models.CASCADE,blank=True,null=True, verbose_name="الفيديو")
    JudgementComity = models.ForeignKey(JudgementComitys, on_delete=models.CASCADE, verbose_name="لجنة التحكيم")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="أسم المستخدم")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التتسجيل")
    is_log = models.BooleanField(default=True, verbose_name="تسجيل")
    is_approval = models.BooleanField(default=True, verbose_name="موافقة")
    is_active = models.BooleanField(default=True, verbose_name="موافقة نشر")
    is_admin = models.BooleanField(default=False, verbose_name="لجنة التحكيم")
    is_staff = models.BooleanField(default=False, verbose_name="انتهاء")

    class Meta:
        verbose_name = "المتسابقين"
        verbose_name_plural = "المتسابقين"

    def __str__(self):
        return self.title








