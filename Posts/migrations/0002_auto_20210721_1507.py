# Generated by Django 3.2.4 on 2021-07-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_Site_1',
            field=models.BooleanField(default=False, verbose_name='قسم الاول'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_Site_2',
            field=models.BooleanField(default=False, verbose_name='قسم الثاني'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_Site_3',
            field=models.BooleanField(default=False, verbose_name='قسم الثالث'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_Site_4',
            field=models.BooleanField(default=False, verbose_name='قسم الرابع'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_Site_5',
            field=models.BooleanField(default=False, verbose_name='قسم الخامس'),
        ),
    ]
