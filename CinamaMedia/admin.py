from django.contrib import admin
from .models import YouTubeTypes,YouTube,LecturesTypes,Lectures,CinamaMedias
from .forms import YouTubeFormAll,LecturesFormAll
# Register your models here.
admin.site.register(YouTubeTypes)
admin.site.register(LecturesTypes)
admin.site.register(CinamaMedias)
class YouTubeAdmin(admin.ModelAdmin):
    list_display = ('title','YouTubeType','author','created','is_active','is_staff','is_admin')
    list_filter = ('created','YouTubeType','is_active','is_staff','is_admin')
    search_fields = ('title','author')
    form = YouTubeFormAll

admin.site.register(YouTube,YouTubeAdmin)

class LecturesAdmin(admin.ModelAdmin):
    list_display = ('title','LecturesType','profile','Date','Time','content','is_active')
    list_filter = ('created','LecturesType','Date')
    search_fields = ('title','profile')
    form = LecturesFormAll

admin.site.register(Lectures,LecturesAdmin)

