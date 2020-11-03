from django.contrib import admin
from .models import Article

# Register your models here
class ArtcleAdmin(admin.ModelAdmin):
    list_display = ('id','title','create_time',)
    list_display_links = ('title',)

admin.site.register(Article,ArtcleAdmin)



