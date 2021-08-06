from django.contrib import admin
from .models import *
from .forms import VideoFilesFormAll


# Register your models here.

class VideoFilesAdmin(admin.ModelAdmin):
    list_display = ('channel','video','title')

    search_fields = ('channel',)
    form = VideoFilesFormAll

admin.site.register(VideoFiles,VideoFilesAdmin)


admin.site.register(Sections)

admin.site.register(MovieSection)

admin.site.register(Stages)

admin.site.register(VideoComment)

admin.site.register(ViewCount)



