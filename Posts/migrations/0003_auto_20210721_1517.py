# Generated by Django 3.2.4 on 2021-07-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20210721_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='موافقة نشر'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='المدير'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='التميز'),
        ),
    ]
