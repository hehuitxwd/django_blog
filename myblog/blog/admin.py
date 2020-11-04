from django.contrib import admin
from .models import Article,Tag,Tui,Category,Banner,Link

# Register your models here
@admin.register(Article)
class ArtcleAdmin(admin.ModelAdmin):
    #文章列表中想要显示的字段
    list_display = ('id','title','create_time',)
    ##满十条数据了就自动分页
    list_per_page = 10
    #后台列表排序方式
    ordering = ('-create_time',)
    ##设置哪些字段点击可以进入到编辑界面
    list_display_links = ('title',)

#admin.site.register(Article,ArtcleAdmin)
#将字段注册到数据库，以便增删改查
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','linkurl')



