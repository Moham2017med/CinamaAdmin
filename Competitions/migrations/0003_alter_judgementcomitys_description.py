# Generated by Django 3.2.4 on 2021-07-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Competitions', '0002_judgementracer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgementcomitys',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='من انا'),
        ),
    ]
