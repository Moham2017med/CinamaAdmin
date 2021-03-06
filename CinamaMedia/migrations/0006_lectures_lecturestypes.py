# Generated by Django 3.2.4 on 2021-07-22 15:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProfileSite', '0001_initial'),
        ('CinamaMedia', '0005_auto_20210721_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='LecturesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LecturesType', models.CharField(max_length=50, verbose_name='قسم الفيديو')),
                ('is_Site_1', models.BooleanField(default=False, verbose_name='قسم الاول')),
                ('is_Site_2', models.BooleanField(default=False, verbose_name='قسم الثاني')),
                ('is_Site_3', models.BooleanField(default=False, verbose_name='قسم الثالث')),
                ('is_Site_4', models.BooleanField(default=False, verbose_name='قسم الرابع')),
                ('is_Site_5', models.BooleanField(default=False, verbose_name='قسم الخامس')),
            ],
            options={
                'verbose_name': 'نواع المحاضرات',
                'verbose_name_plural': 'نواع المحاضرات',
            },
        ),
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='العنوان')),
                ('linke', models.TextField(verbose_name='رابط المحاضرة')),
                ('content', models.TextField(verbose_name='وصف المحاضرة')),
                ('image', models.ImageField(blank=True, upload_to='Lectures/%Y%/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='رفع الصورة')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='تاريخ المحاضرة')),
                ('Time', models.TimeField(auto_now=True, verbose_name='وقت المحاضرة')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تتاريخ التحديث')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ التتسجيل')),
                ('is_active', models.BooleanField(default=True, verbose_name='موافقة نشر')),
                ('is_admin', models.BooleanField(default=False, verbose_name='الادارة')),
                ('is_staff', models.BooleanField(default=False, verbose_name='التميز')),
                ('LecturesType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CinamaMedia.lecturestypes', verbose_name='نوع المحاضرة')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lectures', to='ProfileSite.profile', verbose_name='أسم المحاضر')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lecturesauthor', to=settings.AUTH_USER_MODEL, verbose_name='أسم المستخدم')),
            ],
            options={
                'verbose_name': 'المحاضرات',
                'verbose_name_plural': 'المحاضرات',
            },
        ),
    ]
