# Generated by Django 3.2.4 on 2021-07-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CinamaMedia', '0003_auto_20210721_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubetypes',
            name='is_Site_5',
            field=models.BooleanField(default=True, verbose_name='قسم الخامس'),
        ),
    ]
