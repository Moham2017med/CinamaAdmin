# Generated by Django 3.2.4 on 2021-07-25 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileSite', '0001_initial'),
        ('Posts', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='المستخدم', to='ProfileSite.profile'),
        ),
    ]