import uuid
from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from ProfileSite.models import  Profile as Channel
from ProfileSite.models import  Specialty,SpecialtyType


User = settings.AUTH_USER_MODEL

class Sections(models.Model):
    Section = models.CharField(max_length=200, verbose_name="الموسم")
    is_active = models.BooleanField(default=False, verbose_name="الحالة")

    class Meta:
        verbose_name = "الموسم"
        verbose_name_plural = "الموسم"

    def __str__(self):
        return self.Section

class MovieSection(models.Model):
    MovieSections = models.CharField(max_length=200, verbose_name="أقسام المسابقة")
    is_active = models.BooleanField(default=False, verbose_name="الحالة")

    class Meta:
        verbose_name = "أقسام المسابقة"
        verbose_name_plural = "أقسام المسابقة"

    def __str__(self):
        return self.MovieSections

class Stages(models.Model):
    Stage = models.CharField(max_length=50, verbose_name="مراحل المسابقة")
    Section = models.ForeignKey(Sections, on_delete=models.CASCADE, null=True, verbose_name="الموسم")
    is_active = models.BooleanField(default=False, verbose_name="الحالة")
    is_Site_1 = models.BooleanField(default=False, verbose_name="قسم الاول")
    is_Site_2 = models.BooleanField(default=False, verbose_name="قسم الثاني")
    is_Site_3 = models.BooleanField(default=False, verbose_name="قسم الثالث")
    is_Site_4 = models.BooleanField(default=False, verbose_name="قسم الرابع")
    is_Site_5 = models.BooleanField(default=False, verbose_name="قسم الخامس")

    class Meta:
        verbose_name = "مراحل المسابقة"
        verbose_name_plural = "مراحل المسابقة"

    def __str__(self):
        return self.Stage

class VideoFiles(models.Model):
    title = models.CharField(max_length=200,default="فيديو١", verbose_name="العنوان")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Section = models.ForeignKey(Sections, on_delete=models.CASCADE, default=1, verbose_name="الموسم")
    Stages = models.ForeignKey(Stages, on_delete=models.CASCADE, default=1, verbose_name="مراحل المسابقة")
    MovieSections = models.ForeignKey(MovieSection,default=1, on_delete=models.CASCADE, verbose_name="قسم المسابقة")
    video = models.FileField(upload_to="VideoApp/Video/%Y%/%m/%d")
    SpecialtyType = models.ForeignKey(SpecialtyType, on_delete=models.CASCADE,default=1, verbose_name="نوع التخصص")
    Specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE,default=1, verbose_name="التخصص")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="video_loved")
    dislikes = models.ManyToManyField(User, related_name="video_disliked")
    description = models.TextField(verbose_name="وصف الفيديو")
    visibility = models.BooleanField(choices=((False, "خاص"), (True, "عام")), verbose_name="حالة الفيديو")
    thumbnail = models.ImageField(upload_to="VideoApp/Img/%Y%/%m/%d", verbose_name="صورة الفيديو")
    is_active = models.BooleanField(default=True, verbose_name="موافقة نشر")
    is_admin = models.BooleanField(default=False, verbose_name="المدير")
    is_staff = models.BooleanField(default=False, verbose_name="التميز")

    class Meta:
        verbose_name = "ملف التحمل"
        verbose_name_plural = "ملف التحمل"

    def __str__(self):
        return f"video_file_{self.id}"

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('video_watch', args=[str(self.id)])

    def num_likes(self):
        return self.likes.count()

    def num_dislikes(self):
        return self.dislikes.count()


class ViewCount(models.Model):
    video = models.ForeignKey(VideoFiles, related_name="view_count", on_delete=models.CASCADE, verbose_name="الفيديو")
    ip_address = models.CharField(max_length=50, verbose_name="اي بي")
    session = models.CharField(max_length=50, verbose_name="مشاهدة")

    class Meta:
        verbose_name = "المشاهدات"
        verbose_name_plural = "المشاهدات"

    def __str__(self):
        return f"{self.ip_address}"


class VideoComment(models.Model):
    video = models.ForeignKey(VideoFiles, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "تعليقات"
        verbose_name_plural = "تعليقات"

    def __str__(self):
        return f"{self.user.username} comment"

"""
class Participant(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="الاسم")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="أسم المستخدم")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التتسجيل")
    is_log = models.BooleanField(default=True, verbose_name="تسجيل")
    is_approval = models.BooleanField(default=True, verbose_name="موافقة")
    is_active = models.BooleanField(default=True, verbose_name="موافقة نشر")
    is_admin = models.BooleanField(default=False, verbose_name="الادارة")
    is_staff = models.BooleanField(default=False, verbose_name="انتهاء")

    class Meta:
        verbose_name = "المتسابقين"
        verbose_name_plural = "المتسابقين"

    def __str__(self):
        return self.title
"""


